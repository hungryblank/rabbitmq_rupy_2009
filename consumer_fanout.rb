%w(rubygems mq).each { |lib| require lib }

AMQP.start do

  xchange = MQ.fanout('clock')
  queue = MQ.queue("consumer-#{Process.pid}", :exclusive => true)
  queue.bind(xchange)

  queue.subscribe do |message|
    puts message
  end

end
