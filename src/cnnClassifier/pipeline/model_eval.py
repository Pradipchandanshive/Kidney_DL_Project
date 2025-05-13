import sys
import os
sys.path.append(os.getcwd()) 

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_eval_04 import Evaluation
from cnnClassifier import logger
import os
#import mlflow


STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/Pradipchandanshive/Kidney_DL_Project.mlflow"
        # os.environ["MLFLOW_TRACKING_USERNAME"]="Pradipchandanshive"
        # os.environ["MLFLOW_TRACKING_PASSWORD"]="fd872e30a5f152a078820e8a236b9d00765a27fa"

        # # # Set MLflow tracking URI
        # mlflow.set_tracking_uri("https://dagshub.com/Pradipchandanshive/Kidney_DL_Project.mlflow")
        # evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
 
    