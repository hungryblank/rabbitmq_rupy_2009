require 'rubygems'
require 'mq'

AMQP.start do

  xchange = MQ.fanout('clock')

  EM.add_periodic_timer(1) do
    xchange.publish("it's #{Time.now.to_i}")
  end

end
