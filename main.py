from src.data_integration.data_processor import DataProcessor
from src.ai_engine.llm_interface import LLMInterface
from src.simulation.climate_simulator import ClimateSimulator
import pandas as pd
import numpy as np

def main():
    print("\n--- EcoSphere-Intel-AI Platform Initialization ---")

    # 1. Initialize Data Processor
    data_processor = DataProcessor()

    # 2. Load and Integrate Data (Dummy Data for demonstration)
    print("\n--- Data Loading and Integration ---")
    satellite_data = data_processor.load_satellite_data("path/to/dummy_satellite.tif")
    sensor_data = pd.DataFrame({
        'timestamp': pd.to_datetime(np.arange(10), unit='D', origin='2023-01-01'),
        'temperature': np.random.rand(10) * 30 + 15, # Avg temp 15-45
        'humidity': np.random.rand(10) * 100
    })
    integrated_data = data_processor.integrate_environmental_data(satellite_data, sensor_data)
    print("Integrated Data Sample:\n", integrated_data.head())

    # 3. Initialize LLM Interface
    llm_interface = LLMInterface()

    # 4. Initialize Climate Simulator
    climate_simulator = ClimateSimulator()

    print("\n--- User Interaction Simulation (via LLM) ---")
    user_query = "What would be the impact on global temperature and sea level if deforestation in the Amazon increases by 10% and carbon emissions are reduced by 5% over 30 years?"
    print(f"User Query: '{user_query}'")

    # LLM parses the query and extracts simulation parameters
    # (This is a simplified placeholder for actual LLM parsing)
    # In a real system, the LLM would dynamically generate these parameters
    # based on its understanding of the query and available simulation models.
    extracted_params = {
        "deforestation_rate": 0.10, # 10% increase
        "emission_reduction": 0.05, # 5% reduction
        "duration_years": 30
    }
    print(f"LLM extracted simulation parameters: {extracted_params}")

    # 5. Run Simulation based on LLM-parsed query
    print("\n--- Running Climate Simulation ---")
    simulation_results = climate_simulator.run_scenario_simulation(
        scenario_params={
            "deforestation_rate": extracted_params["deforestation_rate"],
            "emission_reduction": extracted_params["emission_reduction"]
        },
        duration_years=extracted_params["duration_years"]
    )
    print("Simulation Results:", simulation_results)

    # 6. LLM generates policy recommendation based on simulation results
    print("\n--- Generating Policy Recommendation ---")
    policy_recommendation = llm_interface.generate_policy_recommendation(
        simulation_results=str(simulation_results),
        current_policies="Existing policies focus on reforestation and renewable energy incentives."
    )
    print("Policy Recommendation:\n", policy_recommendation)

    print("\n--- EcoSphere-Intel-AI Workflow Completed ---")

if __name__ == "__main__":
    main()
