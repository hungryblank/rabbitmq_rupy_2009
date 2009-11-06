require 'rubygems'
require 'mq'

AMQP.start do
  MQ.prefetch(1)
  queue = MQ.queue('sport')

  queue.subscribe(:ack => true) do |header, news|
    puts "sport: '#{news}'"
    header.ack
  end

end
