class AiAgentService
  include HTTParty
  base_uri ENV.fetch('AI_SERVICE_URL', 'http://localhost:8000')

  def self.ask(store_id, question)
    options = {
      body: {
        store_id: store_id,
        question: question
      }.to_json,
      headers: {
        'Content-Type' => 'application/json',
        'Authorization' => "Bearer #{ENV['Example_Internal_Secret']}" # Optional security
      }
    }

    post("/ask", options)
  end
end
