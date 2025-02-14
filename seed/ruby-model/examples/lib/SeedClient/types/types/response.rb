# frozen_string_literal: true

require "json"

module SeedClient
  module Types
    class Response
      attr_reader :response, :additional_properties

      # @param response [Object]
      # @param additional_properties [OpenStruct] Additional properties unmapped to the current class definition
      # @return [Types::Response]
      def initialize(response:, additional_properties: nil)
        # @type [Object]
        @response = response
        # @type [OpenStruct] Additional properties unmapped to the current class definition
        @additional_properties = additional_properties
      end

      # Deserialize a JSON object to an instance of Response
      #
      # @param json_object [JSON]
      # @return [Types::Response]
      def self.from_json(json_object:)
        struct = JSON.parse(json_object, object_class: OpenStruct)
        response = struct.response
        new(response: response, additional_properties: struct)
      end

      # Serialize an instance of Response to a JSON object
      #
      # @return [JSON]
      def to_json(*_args)
        { "response": @response }.to_json
      end

      # Leveraged for Union-type generation, validate_raw attempts to parse the given hash and check each fields type against the current object's property definitions.
      #
      # @param obj [Object]
      # @return [Void]
      def self.validate_raw(obj:)
        obj.response.is_a?(Object) != false || raise("Passed value for field obj.response is not the expected type, validation failed.")
      end
    end
  end
end
