# frozen_string_literal: true

require "json"

module SeedClient
  module Types
    class Request
      attr_reader :request, :additional_properties

      # @param request [Object]
      # @param additional_properties [OpenStruct] Additional properties unmapped to the current class definition
      # @return [Types::Request]
      def initialize(request:, additional_properties: nil)
        # @type [Object]
        @request = request
        # @type [OpenStruct] Additional properties unmapped to the current class definition
        @additional_properties = additional_properties
      end

      # Deserialize a JSON object to an instance of Request
      #
      # @param json_object [JSON]
      # @return [Types::Request]
      def self.from_json(json_object:)
        struct = JSON.parse(json_object, object_class: OpenStruct)
        request = struct.request
        new(request: request, additional_properties: struct)
      end

      # Serialize an instance of Request to a JSON object
      #
      # @return [JSON]
      def to_json(*_args)
        { "request": @request }.to_json
      end

      # Leveraged for Union-type generation, validate_raw attempts to parse the given hash and check each fields type against the current object's property definitions.
      #
      # @param obj [Object]
      # @return [Void]
      def self.validate_raw(obj:)
        obj.request.is_a?(Object) != false || raise("Passed value for field obj.request is not the expected type, validation failed.")
      end
    end
  end
end
