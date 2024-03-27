from pyspark.sql.streaming import StreamingQuery
from sensa_data_pipelines.executors.pyspark.mixins.profiles_sdk_mixins import (
    ProfilesSdkMixin,
    DataEndpointProfilesSdkMixin,
)
from sensa_data_pipelines.pipeline_model import SensaDataModelConfig, SensaConnectionConfig
from sensa_data_pipelines.executors.pyspark.streaming import StreamingBlock


class Test_Streaming_Bronze_Block(StreamingBlock, ProfilesSdkMixin, DataEndpointProfilesSdkMixin):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def execute_stream(self, **kwargs) -> StreamingQuery:
        kafka_connection = self.get_input_config("from_kafka", SensaConnectionConfig)
        stream_pair = (
            self.sensa.readStream()
            .readConnection(kafka_connection.endpoint.project, kafka_connection.endpoint.name)
            .load()
        )
        bronze_model = self.get_output_config("to_bronze", SensaDataModelConfig)

        return (
            stream_pair.getStreamDf()
            .writeStream.format("delta")
            .queryName(bronze_model.paths.segment)
            .outputMode("append")
            .option("checkpointLocation", bronze_model.paths.checkpoint_path)
            .trigger(processingTime="10 seconds")
            .start(bronze_model.paths.location)
        )
