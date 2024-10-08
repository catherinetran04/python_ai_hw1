import sys 
sys.path.append('aima-python')
from agents import *

class VaccumAgents:
    """
    Run the ReflexVacuumAgent in the TrivialVacuumEnvironment for 15 steps. Use the
    TraceAgent class to print out its perceptions and actions at each time step. Return
    the environment status.
    """
    def reflex_vacuum_agent(self):

        agent = ReflexVacuumAgent()
        TraceAgent(agent)

        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status

    """
    Run the ModelBasedVacuumAgent in the TrivialVacuumEnvironment for 15 steps.
    Use the TraceAgent class to print out its perceptions and actions at each time step.
    Return the environment status.
    """
    def model_based_vacuum_agent(self):

        agent = ModelBasedVacuumAgent()
        TraceAgent(agent)

        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status
        
    """
    Run the RandomVacuumAgent agent in the TrivialVacuumEnvironment for 15 steps.
    Use the TraceAgent class to print out its perceptions and actions at each time step.
    Return the environment status.
    """
    def random_vacuum_agent(self):

        agent = RandomVacuumAgent()
        TraceAgent(agent)

        environment = TrivialVacuumEnvironment()
        environment.add_thing(agent)
        environment.run(15)
        return environment.status

    """
    Use the compare agents function to compare the three agents in the trivial environment. Return the results of the comparison.
    """
    def compare(self):
        environment = TrivialVacuumEnvironment
        agents = [ModelBasedVacuumAgent, RandomVacuumAgent, ReflexVacuumAgent]
        result = compare_agents(environment, agents)
        return result


def main():
    vc = VaccumAgents()
    print("Reflex: ", vc.reflex_vacuum_agent())
    print("Model: ", vc.model_based_vacuum_agent())
    print("Random: ", vc.random_vacuum_agent())
    print("Compare: ", vc.compare())

if __name__ == '__main__':
    main()
