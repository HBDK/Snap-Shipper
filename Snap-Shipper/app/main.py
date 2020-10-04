from os import listdir
from os.path import isfile, join
from Options import OptionsBuilder
from SinkFactory import SinkFactory
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)
logging.info("Starting Snap-Shipper")

options = OptionsBuilder().Options

if options.DryRun:
    logging.warning("Dry run so we son't ship anything")

clients =  SinkFactory(options.Sinks).Sinks

for file in listdir(options.Folder):
    path = join(options.Folder,file)
    logging.info("Processing: {}".format(path))
    if isfile(path):
        for client in clients:
            if not file in client.Remotes:
                logging.info("uploading: {} To: {}".format(file,client.Name))
                if not options.DryRun:
                    client.Upload(remote_path=file, local_path=path)
            else:
                logging.info("Skipping: {} for: {}".format(file,client.Name))
