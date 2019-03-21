import trulogger


logger = trulogger.TruLogger({'verbose': True})

logger.set_prefix("custom prefix")

logger.info("This is info")
logger.error("This is error")
logger.warning("This is warning")
logger.debug("This is debug")
logger.success("This is an success")

logger.add_to_log("This is a simple add")

logger2 = trulogger.TruLogger({'verbose': True, 'traceback': True})

logger2.set_prefix("custom prefix")

logger2.info("This is info")
logger2.reset_prefix()
logger2.error("This is error")
logger2.warning("This is warning")
logger2.debug("This is debug")
logger2.success("This is an success")

logger2.add_to_log("This is a simple add")