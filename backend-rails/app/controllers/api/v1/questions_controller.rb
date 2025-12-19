module Api
  module V1
    class QuestionsController < ApplicationController
      # POST /api/v1/questions
      def create
        store_id = params[:store_id]
        question = params[:question]

        unless store_id && question
          render json: { error: "Missing store_id or question" }, status: :unprocessable_entity
          return
        end

        # In a real app, we would validate the shopify token here
        # verify_shopify_request!

        begin
          # Call the Python AI Service
          response = AiAgentService.ask(store_id, question)
          
          if response.success?
            render json: response.parsed_response, status: :ok
          else
            render json: { error: "AI Service failed", details: response.body }, status: :bad_gateway
          end
        rescue StandardError => e
          render json: { error: e.message }, status: :internal_server_error
        end
      end
    end
  end
end
