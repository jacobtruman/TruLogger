import trulogger


logger = trulogger.TruLogger({'verbose': True})

logger.set_prefix("custom prefix")

logger.info("This is info")
logger.error("This is error")
logger.warning("This is warning")
logger.debug("This is debug")
logger.success("This is an success")

logger.add_to_log("This is a simple add")
