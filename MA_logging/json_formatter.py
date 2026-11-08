import logging
import json
class Json_Formatter(logging.Formatter):
    def format(self,record):
        log_data = dict(
            asctime=self.formatTime(record,self.datefmt),
            level= record.levelname,
            name=record.name,
            message= record.getMessage()
            )

            
        return json.dumps(log_data)

json_logger = logging.getLogger(__name__)
json_logger.setLevel(level=logging.DEBUG)
file_hadler = logging.FileHandler('ma_log.jsonl','a')
file_hadler.setFormatter(Json_Formatter())
json_logger.addHandler(file_hadler)

