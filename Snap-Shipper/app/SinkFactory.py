from webdavclient import WebDavClient
import logging

class SinkFactory:
    def __init__(self,sinks):
        self.Sinks = []
        for sink in sinks:
            keys = sink.keys()

            if not "Name" in keys:
                logging.warning("Sink missing name:\n" + str(sink))
                continue

            if "WebDavClient" in keys:
                logging.debug("Adding WebDav Sink: {}".format(sink["Name"]))
                try:
                    client = WebDavClient(sink)
                except Exception as err:
                    logging.warning("Couldn't create sink {} skipping \n{}:\n{}".format(sink["Name"],type(err).__name__,err))
                    continue
                
                self.Sinks.append(client)
                continue

            logging.warning("Couldn't create sink for:\n" + str(sink))
        
        if not self.Sinks:
            logging.error("couldn't create any sinks, exiting")
            exit()
