"""
You can run this example like this:

    .. code:: console

            $ luigi --module examples.hello_world examples.HelloWorldTask --local-scheduler

If that does not work, see :ref:`CommandLine`.
"""
import luigi


class IngestJobTask(luigi.Task):

    customer_id = luigi.Parameter()
    trace_id = luigi.Parameter()

    accepts_messages = True


    def run(self):
    	import time
    	time.sleep(100)
        print("{task} says: Hello world!".format(task=self.__class__.__name__))


if __name__ == '__main__':
    luigi.run(['examples.HelloWorldTask', '--workers', '1', '--local-scheduler'])
