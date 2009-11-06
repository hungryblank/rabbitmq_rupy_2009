require 'rubygems'
require 'mq'

AMQP.start do
  
  queue = MQ.queue('sport')

  EM.add_periodic_timer(1) do
    queue.publish("some footballer kicked a ball")
  end

end
