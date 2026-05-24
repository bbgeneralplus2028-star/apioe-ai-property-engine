from agents.property_agent import PropertyAgent
from agents.legal_agent import LegalAgent
from agents.equity_agent import EquityAgent
from agents.opportunity_agent import OpportunityAgent

class Orchestrator:

    def run_full_analysis(self, address):
        property_data = PropertyAgent().fetch(address)
        legal_data = LegalAgent().scan(property_data)
        equity = EquityAgent().calculate(property_data)
        opportunity = OpportunityAgent().score(property_data, equity, legal_data)

        return {
            "property": property_data,
            "legal": legal_data,
            "equity": equity,
            "opportunity": opportunity
        }
