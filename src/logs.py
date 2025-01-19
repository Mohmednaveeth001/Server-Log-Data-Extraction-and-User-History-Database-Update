import logging

def setup_logging():
    """Set up logging configuration for the pipeline."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("data/pipeline.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("PipelineLogger")
