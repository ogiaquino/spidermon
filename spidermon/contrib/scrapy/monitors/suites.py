from spidermon import MonitorSuite

from .monitors import (
    DownloaderExceptionMonitor,
    ErrorCountMonitor,
    FieldCoverageMonitor,
    FinishReasonMonitor,
    ItemCountMonitor,
    ItemValidationMonitor,
    PeriodicExecutionTimeMonitor,
    PeriodicItemCountMonitor,
    RetryCountMonitor,
    SuccessfulRequestsMonitor,
    TotalRequestsMonitor,
    UnwantedHTTPCodesMonitor,
    WarningCountMonitor,
)


class SpiderCloseMonitorSuite(MonitorSuite):
    """This Monitor Suite implements the following monitors:

    * :class:`.monitors.ItemCountMonitor`
    * :class:`.monitors.ItemValidationMonitor`
    * :class:`.monitors.ErrorCountMonitor`
    * :class:`.monitors.WarningCountMonitor`
    * :class:`.monitors.FinishReasonMonitor`
    * :class:`.monitors.UnwantedHTTPCodesMonitor`
    * :class:`.monitors.FieldCoverageMonitor`
    * :class:`.monitors.RetryCountMonitor`
    * :class:`.monitors.DownloaderExceptionMonitor`
    * :class:`.monitors.SuccessfulRequestsMonitor`
    * :class:`.monitors.TotalRequestsMonitor`

    You can easily enable this monitor *after* enabling Spidermon::

            SPIDERMON_SPIDER_CLOSE_MONITORS = (
                'spidermon.contrib.scrapy.monitors.SpiderCloseMonitorSuite',
            )
    """

    monitors = [
        ItemCountMonitor,
        ItemValidationMonitor,
        ErrorCountMonitor,
        WarningCountMonitor,
        FinishReasonMonitor,
        UnwantedHTTPCodesMonitor,
        FieldCoverageMonitor,
        RetryCountMonitor,
        DownloaderExceptionMonitor,
        SuccessfulRequestsMonitor,
        TotalRequestsMonitor,
    ]


class PeriodicMonitorSuite(MonitorSuite):
    """This Monitor Suite implements the following monitors:

    * :class:`.monitors.PeriodicExecutionTimeMonitor`

    You can easily enable this monitor *after* enabling Spidermon::

            SPIDERMON_PERIODIC_MONITORS = {
                'spidermon.contrib.scrapy.monitors.PeriodicMonitorSuite': # check time in seconds,
            }
    """

    monitors = [PeriodicExecutionTimeMonitor]


class PeriodicItemCountMonitorSuite(MonitorSuite):
    """This Monitor Suite implements the following monitors:

    * :class:`.monitors.PeriodicExecutionTimeMonitor`

    You can easily enable this monitor *after* enabling Spidermon::

            SPIDERMON_PERIODIC_MONITORS = {
                'spidermon.contrib.scrapy.monitors.PeriodicItemCountMonitorSuite': # check time in seconds,
            }
    """

    monitors = [PeriodicItemCountMonitor]
