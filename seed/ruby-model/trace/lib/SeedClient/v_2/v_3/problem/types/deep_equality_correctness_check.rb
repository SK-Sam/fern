# frozen_string_literal: true

require_relative "parameter_id"
require "json"

module SeedClient
  module V2
    module V3
      module Problem
        class DeepEqualityCorrectnessCheck
          attr_reader :expected_value_parameter_id, :additional_properties

          # @param expected_value_parameter_id [V2::V3::Problem::PARAMETER_ID]
          # @param additional_properties [OpenStruct] Additional properties unmapped to the current class definition
          # @return [V2::V3::Problem::DeepEqualityCorrectnessCheck]
          def initialize(expected_value_parameter_id:, additional_properties: nil)
            # @type [V2::V3::Problem::PARAMETER_ID]
            @expected_value_parameter_id = expected_value_parameter_id
            # @type [OpenStruct] Additional properties unmapped to the current class definition
            @additional_properties = additional_properties
          end

          # Deserialize a JSON object to an instance of DeepEqualityCorrectnessCheck
          #
          # @param json_object [JSON]
          # @return [V2::V3::Problem::DeepEqualityCorrectnessCheck]
          def self.from_json(json_object:)
            struct = JSON.parse(json_object, object_class: OpenStruct)
            expected_value_parameter_id = struct.expectedValueParameterId
            new(expected_value_parameter_id: expected_value_parameter_id, additional_properties: struct)
          end

          # Serialize an instance of DeepEqualityCorrectnessCheck to a JSON object
          #
          # @return [JSON]
          def to_json(*_args)
            { "expectedValueParameterId": @expected_value_parameter_id }.to_json
          end

          # Leveraged for Union-type generation, validate_raw attempts to parse the given hash and check each fields type against the current object's property definitions.
          #
          # @param obj [Object]
          # @return [Void]
          def self.validate_raw(obj:)
            obj.expected_value_parameter_id.is_a?(String) != false || raise("Passed value for field obj.expected_value_parameter_id is not the expected type, validation failed.")
          end
        end
      end
    end
  end
end
