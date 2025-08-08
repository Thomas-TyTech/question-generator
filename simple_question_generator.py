import json
import random
from typing import List, Dict, Any
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class TestQuestion:
    id: str
    question: str
    category: str
    subcategory: str = ""
    complexity: str = "basic"
    priority: str = "medium"
    user_persona: str = "general"
    state: str = "SC"

class SimpleQuestionGenerator:
    
    def __init__(self, state="SC", state_name="South Carolina"):
        self.state = state
        self.state_name = state_name
        self.categories = self._get_state_categories()
        self.user_personas = [
            "general", "senior_citizen", "small_business_owner", "college_student", 
            "new_resident", "veteran", "parent", "unemployed_person", "disabled_person"
        ]
        self.question_templates = self._get_state_question_templates()
        
    def _get_state_categories(self) -> Dict[str, Any]:
        base_categories = {
            "government": {
                "subcategories": ["voting", "licenses", "permits", "records", "elected_officials"],
                "complexity_distribution": {"basic": 0.5, "intermediate": 0.3, "complex": 0.2}
            },
            "business": {
                "subcategories": ["registration", "licenses", "permits", "taxes", "regulations"],
                "complexity_distribution": {"basic": 0.4, "intermediate": 0.4, "complex": 0.2}
            },
            "employment": {
                "subcategories": ["unemployment", "job_search", "workers_comp", "labor_rights"],
                "complexity_distribution": {"basic": 0.6, "intermediate": 0.3, "complex": 0.1}
            },
            "healthcare": {
                "subcategories": ["medicaid", "insurance", "public_health", "mental_health"],
                "complexity_distribution": {"basic": 0.5, "intermediate": 0.4, "complex": 0.1}
            },
            "education": {
                "subcategories": ["k12", "higher_ed", "financial_aid", "adult_ed"],
                "complexity_distribution": {"basic": 0.6, "intermediate": 0.3, "complex": 0.1}
            },
            "transportation": {
                "subcategories": ["dmv", "public_transit", "roads", "vehicle_registration"],
                "complexity_distribution": {"basic": 0.7, "intermediate": 0.2, "complex": 0.1}
            },
            "housing": {
                "subcategories": ["assistance", "regulations", "property_tax", "first_time_buyers"],
                "complexity_distribution": {"basic": 0.4, "intermediate": 0.4, "complex": 0.2}
            },
            "taxation": {
                "subcategories": ["income_tax", "property_tax", "business_tax", "tax_assistance"],
                "complexity_distribution": {"basic": 0.3, "intermediate": 0.5, "complex": 0.2}
            },
            "recreation": {
                "subcategories": ["parks", "hunting_fishing", "tourism", "events"],
                "complexity_distribution": {"basic": 0.8, "intermediate": 0.2, "complex": 0.0}
            },
            "seniors": {
                "subcategories": ["benefits", "healthcare", "housing", "transportation"],
                "complexity_distribution": {"basic": 0.6, "intermediate": 0.3, "complex": 0.1}
            }
        }
        
        if self.state == "HI":
            base_categories["environment"] = {
                "subcategories": ["conservation", "marine_life", "hunting_fishing", "permits", "research"],
                "complexity_distribution": {"basic": 0.5, "intermediate": 0.3, "complex": 0.2}
            }
        
        return base_categories
        
    def _get_state_question_templates(self) -> Dict[str, Any]:
        if self.state == "HI":
            return self._get_hawaii_templates()
        elif self.state == "IN":
            return self._get_indiana_templates()
        elif self.state == "MS":
            return self._get_mississippi_templates()
        else:
            return self._get_south_carolina_templates()
    
    def _get_south_carolina_templates(self) -> Dict[str, Any]:
        return {
            "government": {
                "basic": [
                    "How do I register to vote in South Carolina?",
                    "Where can I get a copy of my birth certificate?",
                    "What are the hours for the DMV?",
                    "How do I contact my state representative?",
                    "What documents do I need to get a state ID?",
                    "How do I find my polling location?",
                    "Where can I get a copy of my marriage certificate?",
                    "How do I register my vehicle?",
                    "What are the requirements for a concealed carry permit?",
                    "How do I get a passport in South Carolina?",
                    "Where can I pay my property taxes?",
                    "How do I change my voter registration address?",
                    "What documents do I need for a REAL ID?",
                    "How do I request an absentee ballot?",
                    "Where can I find information about jury duty?"
                ],
                "intermediate": [
                    "What are the requirements for running for local office in South Carolina?",
                    "How do I request public records from a state agency?",
                    "What is the process for appealing a government decision?",
                    "How can I file a complaint against a state employee?",
                    "How do I petition for a new traffic light in my neighborhood?",
                    "What is the process for changing my name legally?",
                    "How do I apply for a notary public commission?",
                    "What are the steps to become a poll worker?",
                    "How do I request a hearing for a code violation?",
                    "What is required to establish a nonprofit organization?",
                    "How do I appeal a property tax assessment?",
                    "What are the requirements for homeschooling registration?"
                ],
                "complex": [
                    "How do I navigate the state procurement process for government contracts?",
                    "What are my rights under South Carolina's Freedom of Information Act?",
                    "How do I petition the state legislature for a new law?",
                    "What is the process for challenging an election result?",
                    "How do I navigate constitutional rights violations by state agencies?",
                    "What are the procedures for whistleblower protection in state government?",
                    "How do I initiate a ballot measure or referendum?",
                    "What are my rights during eminent domain proceedings?"
                ]
            },
            "business": {
                "basic": [
                    "How do I register a business in South Carolina?",
                    "What business licenses do I need to start a restaurant?",
                    "How do I get a tax ID number for my business?",
                    "Where can I find information about business taxes?",
                    "How do I register a DBA (doing business as) name?",
                    "What permits do I need for a food truck?",
                    "How do I get a resale certificate?",
                    "What are the requirements for a home-based business?",
                    "How do I apply for a liquor license?",
                    "What business insurance is required in South Carolina?",
                    "How do I register for workers' compensation?",
                    "What are the steps to dissolve a business?",
                    "How do I get a contractor's license?",
                    "What permits are needed for a beauty salon?",
                    "How do I apply for a retail merchant certificate?"
                ],
                "intermediate": [
                    "What are the zoning requirements for opening a retail store?",
                    "How do I apply for a state business grant?",
                    "What are the worker's compensation requirements for employers?",
                    "How do I register for state sales tax collection?",
                    "What are the requirements for minority business certification?",
                    "How do I comply with ADA requirements for my business?",
                    "What environmental permits do I need for manufacturing?",
                    "How do I handle business closures due to health violations?",
                    "What are the requirements for professional licensing boards?",
                    "How do I set up a business retirement plan?",
                    "What are the export/import regulations for businesses?",
                    "How do I navigate business partnership disputes legally?"
                ],
                "complex": [
                    "What are the environmental regulations for manufacturing businesses?",
                    "How do I comply with state employment law for a multi-location business?",
                    "What are the requirements for government contracting certification?",
                    "How do I navigate complex tax incentive programs for businesses?",
                    "What are the compliance requirements for publicly traded companies?",
                    "How do I handle multi-state business operations and regulations?",
                    "What are the requirements for international business operations?",
                    "How do I navigate intellectual property protections at the state level?"
                ]
            },
            "employment": {
                "basic": [
                    "How do I apply for unemployment benefits?",
                    "Where can I find job training programs?",
                    "How do I file a workplace injury claim?",
                    "What are the minimum wage laws in South Carolina?",
                    "How do I search for state government jobs?",
                    "What are the requirements for temp work agencies?",
                    "How do I get my final paycheck after termination?",
                    "Where can I find apprenticeship programs?",
                    "How do I report unpaid wages?",
                    "What are my rights as a seasonal worker?",
                    "How do I apply for disability benefits?",
                    "Where can I get help with resume writing?",
                    "What job placement services are available?",
                    "How do I verify my employment eligibility?",
                    "What are the child labor laws in South Carolina?"
                ],
                "intermediate": [
                    "How do I report workplace discrimination?",
                    "What retraining programs are available for displaced workers?",
                    "How do I appeal an unemployment benefits denial?",
                    "What are my rights during a workplace investigation?",
                    "How do I file for reasonable accommodation at work?",
                    "What is the process for reporting unsafe working conditions?",
                    "How do I handle workplace harassment complaints?",
                    "What are the requirements for employee leave policies?",
                    "How do I navigate layoffs and plant closures?",
                    "What protections exist for whistleblowers in employment?",
                    "How do I challenge a wrongful termination?",
                    "What are my rights regarding overtime and breaks?"
                ],
                "complex": [
                    "What are my rights under the Family and Medical Leave Act in South Carolina?",
                    "How do I file a complex workers' compensation claim?",
                    "How do I navigate employment law for union activities?",
                    "What are the procedures for employment-related lawsuits?",
                    "How do I handle multi-employer pension plan issues?",
                    "What are the requirements for executive compensation disclosure?",
                    "How do I navigate employment contracts and non-compete agreements?",
                    "What are the complex disability accommodation requirements?"
                ]
            },
            "healthcare": {
                "basic": [
                    "How do I apply for Medicaid in South Carolina?",
                    "Where can I find free health clinics?",
                    "How do I get help with prescription drug costs?",
                    "What mental health services are available?",
                    "How do I find dental care assistance programs?",
                    "Where can I get immunizations for my children?",
                    "How do I apply for emergency medical assistance?",
                    "What substance abuse treatment programs are available?",
                    "How do I get vision care assistance?",
                    "Where can I find prenatal care services?",
                    "How do I access senior health programs?",
                    "What health screenings are available for free?",
                    "How do I get help with medical transportation?",
                    "Where can I find WIC program information?",
                    "How do I report a healthcare complaint?"
                ],
                "intermediate": [
                    "How do I appeal a Medicaid denial?",
                    "What are the eligibility requirements for state health insurance programs?",
                    "How do I find specialized medical care through state programs?",
                    "What are the requirements for home health aide services?",
                    "How do I navigate Medicare supplement programs?",
                    "What mental health crisis intervention services exist?",
                    "How do I access rehabilitation services after injury?",
                    "What are the procedures for medical disability determinations?",
                    "How do I get second opinions through state programs?",
                    "What are the requirements for nursing home placement?",
                    "How do I navigate health insurance appeals processes?",
                    "What support exists for caregivers of disabled family members?"
                ],
                "complex": [
                    "How do I navigate the state's health insurance marketplace with complex medical needs?",
                    "What are my options for long-term care coverage through state programs?",
                    "How do I coordinate benefits across multiple health programs?",
                    "What are the requirements for experimental treatment coverage?",
                    "How do I navigate medical malpractice complaint processes?",
                    "What are the procedures for healthcare advance directives?",
                    "How do I handle complex disability benefit determinations?",
                    "What are the requirements for medical research participation?"
                ]
            },
            "transportation": {
                "basic": [
                    "How do I renew my driver's license?",
                    "What documents do I need to register my car?",
                    "How much does it cost to get a new license plate?",
                    "Where is the nearest DMV office?",
                    "How do I get a replacement driver's license?",
                    "What are the requirements for a motorcycle license?",
                    "How do I register a boat in South Carolina?",
                    "What do I need to transfer vehicle ownership?",
                    "How do I get a temporary vehicle permit?",
                    "What are the requirements for disabled parking permits?",
                    "How do I report a vehicle accident?",
                    "Where can I find public transportation schedules?",
                    "How do I get a vehicle inspection?",
                    "What are the requirements for teen driver permits?",
                    "How do I contest a parking ticket?"
                ],
                "intermediate": [
                    "How do I transfer my out-of-state license to South Carolina?",
                    "What are the requirements for getting a commercial driver's license?",
                    "How do I contest a traffic ticket?",
                    "What are the procedures for vehicle emission testing?",
                    "How do I get a salvage vehicle title?",
                    "What are the requirements for commercial vehicle registration?",
                    "How do I handle insurance disputes after accidents?",
                    "What are the procedures for license suspension appeals?",
                    "How do I get a restricted license after DUI?",
                    "What are the requirements for driver education programs?",
                    "How do I register an out-of-state vehicle purchase?",
                    "What are the procedures for vehicle lien releases?"
                ],
                "complex": [
                    "How do I get a special permit for transporting oversized loads?",
                    "What are the requirements for becoming a ride-share driver in South Carolina?",
                    "How do I navigate complex commercial transportation regulations?",
                    "What are the procedures for establishing a transportation business?",
                    "How do I handle multi-state commercial driver licensing?",
                    "What are the requirements for hazardous materials transportation?",
                    "How do I navigate vehicle safety compliance for fleet operations?",
                    "What are the procedures for transportation-related legal disputes?"
                ]
            },
            "education": {
                "basic": [
                    "How do I register my child for public school?",
                    "What are the homeschooling requirements in South Carolina?",
                    "How do I apply for college financial aid?",
                    "Where can I find adult education programs?",
                    "What are the requirements for GED testing?",
                    "How do I transfer schools within the district?",
                    "What special education services are available?",
                    "How do I apply for school choice options?",
                    "What are the vaccination requirements for school?",
                    "How do I get transcripts from South Carolina schools?",
                    "What early childhood education programs exist?",
                    "How do I report bullying in schools?",
                    "What are the requirements for teacher certification?",
                    "How do I access free lunch programs?",
                    "What tutoring services are available?"
                ],
                "intermediate": [
                    "How do I appeal a special education placement decision?",
                    "What are the procedures for school disciplinary hearings?",
                    "How do I navigate college admission appeals?",
                    "What are the requirements for professional development for teachers?",
                    "How do I establish a charter school?",
                    "What are the procedures for educational discrimination complaints?",
                    "How do I access vocational rehabilitation services?",
                    "What are the requirements for dual enrollment programs?",
                    "How do I handle custody-related school enrollment issues?",
                    "What are the procedures for educational records disputes?",
                    "How do I navigate homeschool compliance monitoring?",
                    "What support exists for students with disabilities transitioning to college?"
                ],
                "complex": [
                    "How do I navigate special education due process hearings?",
                    "What are the procedures for educational malpractice claims?",
                    "How do I handle complex custody and educational rights disputes?",
                    "What are the requirements for establishing educational foundations?",
                    "How do I navigate federal education compliance issues?",
                    "What are the procedures for teacher tenure and dismissal processes?",
                    "How do I handle complex financial aid and student debt issues?",
                    "What are the requirements for educational research and data collection?"
                ]
            },
            "housing": {
                "basic": [
                    "How do I apply for public housing assistance?",
                    "What are the requirements for first-time homebuyer programs?",
                    "How do I report housing discrimination?",
                    "Where can I find rental assistance programs?",
                    "What are tenant rights in South Carolina?",
                    "How do I apply for housing vouchers?",
                    "What are the requirements for landlord licensing?",
                    "How do I get help with utility deposits?",
                    "What assistance exists for homeless individuals?",
                    "How do I report unsafe housing conditions?",
                    "What are the requirements for mobile home installation?",
                    "How do I access emergency housing assistance?",
                    "What programs help with home repairs?",
                    "How do I understand my lease agreement?",
                    "What are the procedures for security deposit disputes?"
                ],
                "intermediate": [
                    "How do I navigate the eviction process as a tenant?",
                    "What are the requirements for becoming a landlord?",
                    "How do I appeal a housing assistance denial?",
                    "What are the procedures for housing code violations?",
                    "How do I access disability-accessible housing modifications?",
                    "What are the requirements for manufactured housing communities?",
                    "How do I handle neighbor disputes and mediation?",
                    "What are the procedures for rent stabilization programs?",
                    "How do I navigate fair housing complaint processes?",
                    "What are the requirements for senior housing programs?",
                    "How do I access weatherization assistance programs?",
                    "What support exists for transitioning from homelessness?"
                ],
                "complex": [
                    "How do I navigate complex landlord-tenant legal disputes?",
                    "What are the procedures for housing development and zoning appeals?",
                    "How do I handle multi-family housing compliance issues?",
                    "What are the requirements for affordable housing development?",
                    "How do I navigate complex fair housing litigation?",
                    "What are the procedures for housing trust fund applications?",
                    "How do I handle property management licensing and regulations?",
                    "What are the requirements for community land trust development?"
                ]
            },
            "taxation": {
                "basic": [
                    "How do I file my state income tax return?",
                    "What are the property tax rates in my area?",
                    "How do I pay my vehicle taxes?",
                    "Where can I get free tax preparation help?",
                    "What are the sales tax rates in South Carolina?",
                    "How do I appeal my property tax assessment?",
                    "What tax credits are available for families?",
                    "How do I get copies of past tax returns?",
                    "What are the requirements for business tax registration?",
                    "How do I set up a payment plan for back taxes?",
                    "What are the tax implications of retirement income?",
                    "How do I report changes in property ownership?",
                    "What are the requirements for senior tax exemptions?",
                    "How do I handle tax issues after a spouse's death?",
                    "What are the deadlines for various tax filings?"
                ],
                "intermediate": [
                    "How do I navigate tax audits and examinations?",
                    "What are the procedures for tax lien resolution?",
                    "How do I handle multi-state tax obligations?",
                    "What are the requirements for tax-exempt status?",
                    "How do I appeal tax penalties and interest charges?",
                    "What are the procedures for installment agreements?",
                    "How do I navigate business tax compliance for multiple locations?",
                    "What are the requirements for agricultural tax exemptions?",
                    "How do I handle estate and inheritance tax issues?",
                    "What are the procedures for tax refund disputes?",
                    "How do I navigate workers' compensation tax issues?",
                    "What are the requirements for charitable organization tax exemptions?"
                ],
                "complex": [
                    "How do I navigate complex business tax restructuring?",
                    "What are the procedures for tax court litigation?",
                    "How do I handle international tax compliance issues?",
                    "What are the requirements for complex estate tax planning?",
                    "How do I navigate tax implications of business mergers?",
                    "What are the procedures for tax shelter and compliance issues?",
                    "How do I handle complex property tax appeals for commercial properties?",
                    "What are the requirements for tax-advantaged investment structures?"
                ]
            },
            "recreation": {
                "basic": [
                    "How do I get a fishing license in South Carolina?",
                    "What are the hunting seasons and regulations?",
                    "How do I reserve a campsite in state parks?",
                    "Where can I find information about hiking trails?",
                    "What are the requirements for boating licenses?",
                    "How do I get permits for large events in parks?",
                    "What recreational programs are available for seniors?",
                    "How do I register for youth sports programs?",
                    "What are the fees for park admissions?",
                    "How do I report wildlife violations?",
                    "What beach access regulations exist?",
                    "How do I get information about guided tours?",
                    "What are the rules for camping and RVs?",
                    "How do I access disability-friendly recreational facilities?",
                    "What seasonal recreational activities are available?"
                ],
                "intermediate": [
                    "How do I get commercial fishing permits?",
                    "What are the requirements for hunting guide licenses?",
                    "How do I organize charity events in state facilities?",
                    "What are the procedures for environmental education programs?",
                    "How do I get permits for film/photography in parks?",
                    "What are the requirements for recreational vehicle operations?",
                    "How do I navigate liability issues for recreational activities?",
                    "What are the procedures for establishing recreational clubs?",
                    "How do I get permits for water sports and activities?",
                    "What are the requirements for recreational facility management?",
                    "How do I access grants for community recreational programs?",
                    "What are the procedures for recreational safety compliance?"
                ],
                "complex": [
                    "How do I navigate complex environmental regulations for recreational development?",
                    "What are the procedures for establishing new state recreational facilities?",
                    "How do I handle complex liability and insurance issues for recreational businesses?",
                    "What are the requirements for multi-jurisdictional recreational partnerships?",
                    "How do I navigate federal and state coordination for recreational land use?",
                    "What are the procedures for recreational resource conservation planning?",
                    "How do I handle complex permitting for recreational infrastructure development?",
                    "What are the requirements for recreational facility accessibility compliance?"
                ]
            },
            "seniors": {
                "basic": [
                    "What senior services are available in South Carolina?",
                    "How do I apply for senior housing assistance?",
                    "What transportation options exist for seniors?",
                    "How do I get help with prescription drug costs?",
                    "What meal programs are available for seniors?",
                    "How do I apply for senior discounts on utilities?",
                    "What health screenings are available for seniors?",
                    "How do I get help with Medicare enrollment?",
                    "What senior centers are in my area?",
                    "How do I report elder abuse or neglect?",
                    "What social activities are available for seniors?",
                    "How do I get assistance with home modifications?",
                    "What are the requirements for senior property tax exemptions?",
                    "How do I access senior legal aid services?",
                    "What volunteer opportunities exist for seniors?"
                ],
                "intermediate": [
                    "How do I navigate Medicare supplement insurance options?",
                    "What are the procedures for guardianship and conservatorship?",
                    "How do I access adult day care services?",
                    "What are the requirements for nursing home placement?",
                    "How do I handle financial exploitation of seniors?",
                    "What are the procedures for advance healthcare directives?",
                    "How do I navigate long-term care insurance options?",
                    "What support exists for family caregivers?",
                    "How do I access respite care services?",
                    "What are the procedures for senior employment programs?",
                    "How do I navigate retirement benefit coordination?",
                    "What are the requirements for senior housing modifications?"
                ],
                "complex": [
                    "How do I navigate complex estate planning and elder law issues?",
                    "What are the procedures for complex Medicaid planning and asset protection?",
                    "How do I handle multi-generational family care coordination?",
                    "What are the requirements for establishing senior living communities?",
                    "How do I navigate complex disability and aging service coordination?",
                    "What are the procedures for elder abuse prosecution and legal remedies?",
                    "How do I handle complex healthcare decision-making for incapacitated seniors?",
                    "What are the requirements for aging-in-place community development programs?"
                ]
            }
        }
        
    def _get_hawaii_templates(self) -> Dict[str, Any]:
        return {
            "government": {
                "basic": [
                    "How do I register to vote in Hawaii?",
                    "Where can I get a copy of my birth certificate?",
                    "What are the hours for the DMV?",
                    "How do I contact my state representative?",
                    "What documents do I need to get a state ID?"
                ],
                "intermediate": [
                    "What are the requirements for running for local office in Hawaii?",
                    "How do I request public records from a state agency?",
                    "What is the process for appealing a government decision?",
                    "How can I file a complaint against a state employee?"
                ],
                "complex": [
                    "How do I navigate the state procurement process for government contracts?",
                    "What are my rights under Hawaii's Sunshine Law (open meetings)?",
                    "How do I petition the state legislature for a new law?"
                ]
            },
            "business": {
                "basic": [
                    "How do I register a business in Hawaii?",
                    "What business licenses do I need to start a restaurant?",
                    "How do I get a tax ID number for my business?",
                    "Where can I find information about business taxes?"
                ],
                "intermediate": [
                    "What are the zoning requirements for opening a retail store?",
                    "How do I apply for a state business grant?",
                    "What are the worker's compensation requirements for employers?",
                    "How do I register for state sales tax collection?"
                ],
                "complex": [
                    "What are the environmental regulations for manufacturing businesses?",
                    "How do I comply with state employment law for a multi-location business?",
                    "What are the requirements for government contracting certification?"
                ]
            },
            "employment": {
                "basic": [
                    "How do I apply for unemployment benefits?",
                    "Where can I find job training programs?",
                    "How do I file a workplace injury claim?",
                    "What are the minimum wage laws in Hawaii?"
                ],
                "intermediate": [
                    "How do I report workplace discrimination?",
                    "What retraining programs are available for displaced workers?",
                    "How do I appeal an unemployment benefits denial?"
                ],
                "complex": [
                    "What are my rights under the Family and Medical Leave Act in Hawaii?",
                    "How do I file a complex workers' compensation claim?"
                ]
            },
            "healthcare": {
                "basic": [
                    "How do I apply for Medicaid in Hawaii?",
                    "Where can I find free health clinics?",
                    "How do I get help with prescription drug costs?",
                    "What mental health services are available?"
                ],
                "intermediate": [
                    "How do I appeal a Medicaid denial?",
                    "What are the eligibility requirements for state health insurance programs?",
                    "How do I find specialized medical care through state programs?"
                ],
                "complex": [
                    "How do I navigate the state's health insurance marketplace with complex medical needs?",
                    "What are my options for long-term care coverage through state programs?"
                ]
            },
            "transportation": {
                "basic": [
                    "How do I renew my driver's license?",
                    "What documents do I need to register my car?",
                    "How much does it cost to get a new license plate?",
                    "Where is the nearest DMV office?"
                ],
                "intermediate": [
                    "How do I transfer my out-of-state license to Hawaii?",
                    "What are the requirements for getting a commercial driver's license?",
                    "How do I contest a traffic ticket?"
                ],
                "complex": [
                    "How do I get a special permit for transporting oversized loads?",
                    "What are the requirements for becoming a ride-share driver in Hawaii?"
                ]
            },
            "environment": {
                "basic": [
                    "How do I report an environmental concern to DLNR?",
                    "What are the fishing license requirements?",
                    "How do I get a hunting permit in Hawaii?",
                    "Where can I find information about protected marine areas?"
                ],
                "intermediate": [
                    "How do I apply for a permit to conduct research in state waters?",
                    "What are the regulations for commercial fishing?",
                    "How do I report illegal hunting or fishing activities?"
                ],
                "complex": [
                    "What permits do I need for commercial ocean activities?",
                    "How do I apply for an environmental impact assessment?",
                    "What are the requirements for aquaculture operations?"
                ]
            }
        }
        
    def _get_indiana_templates(self) -> Dict[str, Any]:
        return {
            "government": {
                "basic": [
                    "How do I register to vote in Indiana?",
                    "Where can I get a copy of my birth certificate?",
                    "What are the hours for the BMV?",
                    "How do I contact my state representative?",
                    "What documents do I need to get a state ID?"
                ],
                "intermediate": [
                    "What are the requirements for running for local office in Indiana?",
                    "How do I request public records from a state agency?",
                    "What is the process for appealing a government decision?",
                    "How can I file a complaint against a state employee?"
                ],
                "complex": [
                    "How do I navigate the state procurement process for government contracts?",
                    "What are my rights under Indiana's Access to Public Records Act?",
                    "How do I petition the state legislature for a new law?"
                ]
            },
            "business": {
                "basic": [
                    "How do I register a business in Indiana?",
                    "What business licenses do I need to start a restaurant?",
                    "How do I get a tax ID number for my business?",
                    "Where can I find information about business taxes?"
                ],
                "intermediate": [
                    "What are the zoning requirements for opening a retail store?",
                    "How do I apply for a state business grant?",
                    "What are the worker's compensation requirements for employers?",
                    "How do I register for state sales tax collection?"
                ],
                "complex": [
                    "What are the environmental regulations for manufacturing businesses?",
                    "How do I comply with state employment law for a multi-location business?",
                    "What are the requirements for government contracting certification?"
                ]
            },
            "employment": {
                "basic": [
                    "How do I apply for unemployment benefits?",
                    "Where can I find job training programs?",
                    "How do I file a workplace injury claim?",
                    "What are the minimum wage laws in Indiana?"
                ],
                "intermediate": [
                    "How do I report workplace discrimination?",
                    "What retraining programs are available for displaced workers?",
                    "How do I appeal an unemployment benefits denial?"
                ],
                "complex": [
                    "What are my rights under the Family and Medical Leave Act in Indiana?",
                    "How do I file a complex workers' compensation claim?"
                ]
            },
            "healthcare": {
                "basic": [
                    "How do I apply for Medicaid in Indiana?",
                    "Where can I find free health clinics?",
                    "How do I get help with prescription drug costs?",
                    "What mental health services are available?"
                ],
                "intermediate": [
                    "How do I appeal a Medicaid denial?",
                    "What are the eligibility requirements for state health insurance programs?",
                    "How do I find specialized medical care through state programs?"
                ],
                "complex": [
                    "How do I navigate the state's health insurance marketplace with complex medical needs?",
                    "What are my options for long-term care coverage through state programs?"
                ]
            },
            "transportation": {
                "basic": [
                    "How do I renew my driver's license?",
                    "What documents do I need to register my car?",
                    "How much does it cost to get a new license plate?",
                    "Where is the nearest BMV office?"
                ],
                "intermediate": [
                    "How do I transfer my out-of-state license to Indiana?",
                    "What are the requirements for getting a commercial driver's license?",
                    "How do I contest a traffic ticket?"
                ],
                "complex": [
                    "How do I get a special permit for transporting oversized loads?",
                    "What are the requirements for becoming a ride-share driver in Indiana?"
                ]
            }
        }
        
    def _get_mississippi_templates(self) -> Dict[str, Any]:
        return {
            "government": {
                "basic": [
                    "How do I register to vote in Mississippi?",
                    "Where can I get a copy of my birth certificate?",
                    "What are the hours for the DPS?",
                    "How do I contact my state representative?",
                    "What documents do I need to get a state ID?"
                ],
                "intermediate": [
                    "What are the requirements for running for local office in Mississippi?",
                    "How do I request public records from a state agency?",
                    "What is the process for appealing a government decision?",
                    "How can I file a complaint against a state employee?"
                ],
                "complex": [
                    "How do I navigate the state procurement process for government contracts?",
                    "What are my rights under Mississippi's Public Records Act?",
                    "How do I petition the state legislature for a new law?"
                ]
            },
            "business": {
                "basic": [
                    "How do I register a business in Mississippi?",
                    "What business licenses do I need to start a restaurant?",
                    "How do I get a tax ID number for my business?",
                    "Where can I find information about business taxes?"
                ],
                "intermediate": [
                    "What are the zoning requirements for opening a retail store?",
                    "How do I apply for a state business grant?",
                    "What are the worker's compensation requirements for employers?",
                    "How do I register for state sales tax collection?"
                ],
                "complex": [
                    "What are the environmental regulations for manufacturing businesses?",
                    "How do I comply with state employment law for a multi-location business?",
                    "What are the requirements for government contracting certification?"
                ]
            },
            "employment": {
                "basic": [
                    "How do I apply for unemployment benefits?",
                    "Where can I find job training programs?",
                    "How do I file a workplace injury claim?",
                    "What are the minimum wage laws in Mississippi?"
                ],
                "intermediate": [
                    "How do I report workplace discrimination?",
                    "What retraining programs are available for displaced workers?",
                    "How do I appeal an unemployment benefits denial?"
                ],
                "complex": [
                    "What are my rights under the Family and Medical Leave Act in Mississippi?",
                    "How do I file a complex workers' compensation claim?"
                ]
            },
            "healthcare": {
                "basic": [
                    "How do I apply for Medicaid in Mississippi?",
                    "Where can I find free health clinics?",
                    "How do I get help with prescription drug costs?",
                    "What mental health services are available?"
                ],
                "intermediate": [
                    "How do I appeal a Medicaid denial?",
                    "What are the eligibility requirements for state health insurance programs?",
                    "How do I find specialized medical care through state programs?"
                ],
                "complex": [
                    "How do I navigate the state's health insurance marketplace with complex medical needs?",
                    "What are my options for long-term care coverage through state programs?"
                ]
            },
            "transportation": {
                "basic": [
                    "How do I renew my driver's license?",
                    "What documents do I need to register my car?",
                    "How much does it cost to get a new license plate?",
                    "Where is the nearest DPS office?"
                ],
                "intermediate": [
                    "How do I transfer my out-of-state license to Mississippi?",
                    "What are the requirements for getting a commercial driver's license?",
                    "How do I contest a traffic ticket?"
                ],
                "complex": [
                    "How do I get a special permit for transporting oversized loads?",
                    "What are the requirements for becoming a ride-share driver in Mississippi?"
                ]
            }
        }
        
    def generate_questions(self, num_questions: int = 50, 
                          categories: List[str] = None,
                          complexity_override: Dict[str, float] = None) -> List[TestQuestion]:
        
        if categories is None:
            categories = list(self.categories.keys())
        
        questions = []
        questions_per_category = max(1, num_questions // len(categories))
        
        for category in categories:
            category_info = self.categories[category]
            complexity_dist = complexity_override.get(category, category_info["complexity_distribution"]) if complexity_override else category_info["complexity_distribution"]
            
            for _ in range(questions_per_category):
                complexity = self._select_complexity(complexity_dist)
                subcategory = random.choice(category_info["subcategories"])
                question = self._generate_question_for_category(category, complexity, subcategory)
                persona = random.choice(self.user_personas)
                
                test_q = TestQuestion(
                    id=f"Q{len(questions)+1:03d}",
                    question=question,
                    category=category,
                    subcategory=subcategory,
                    complexity=complexity,
                    priority=self._get_priority(complexity),
                    user_persona=persona,
                    state=self.state
                )
                
                questions.append(test_q)
        
        while len(questions) < num_questions:
            category = random.choice(categories)
            category_info = self.categories[category]
            complexity_dist = category_info["complexity_distribution"]
            complexity = self._select_complexity(complexity_dist)
            subcategory = random.choice(category_info["subcategories"])
            
            question = self._generate_question_for_category(category, complexity, subcategory)
            persona = random.choice(self.user_personas)
            
            test_q = TestQuestion(
                id=f"Q{len(questions)+1:03d}",
                question=question,
                category=category,
                subcategory=subcategory,
                complexity=complexity,
                priority=self._get_priority(complexity),
                user_persona=persona,
                state=self.state
            )
            
            questions.append(test_q)
        
        return questions[:num_questions]
    
    def _select_complexity(self, distribution: Dict[str, float]) -> str:
        rand = random.random()
        cumulative = 0
        for complexity, prob in distribution.items():
            cumulative += prob
            if rand <= cumulative:
                return complexity
        return "basic"
    
    def _generate_question_for_category(self, category: str, complexity: str, subcategory: str) -> str:
        templates = self.question_templates.get(category, {}).get(complexity, [])
        
        if templates:
            base_question = random.choice(templates)
            variations = self._get_question_variations(base_question, subcategory)
            return random.choice(variations)
        else:
            return f"What services does {self.state_name} provide for {subcategory.replace('_', ' ')}?"
    
    def _get_question_variations(self, base_question: str, subcategory: str) -> List[str]:
        variations = [base_question]
        
        if "How do I" in base_question:
            variations.append(base_question.replace("How do I", "What's the process to"))
            variations.append(base_question.replace("How do I", "Can you help me"))
        
        if "What are" in base_question:
            variations.append(base_question.replace("What are", "Can you tell me about"))
            variations.append(base_question.replace("What are", "I need information about"))
        
        return variations
    
    def _get_priority(self, complexity: str) -> str:
        priority_map = {
            "basic": "high",
            "intermediate": "medium",
            "complex": "low"
        }
        return priority_map.get(complexity, "medium")
    
    def save_questions(self, questions: List[TestQuestion], filename: str = None) -> str:
        if filename is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"simple_questions_{timestamp}.json"
        
        questions_data = [asdict(q) for q in questions]
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(questions_data, f, indent=2, ensure_ascii=False)
        
        return filename
    
    def generate_focused_test_set(self, focus_area: str, num_questions: int = 20) -> List[TestQuestion]:
        focus_configs = {
            "basic_services": {
                "categories": ["government", "transportation", "recreation"],
                "complexity_override": {cat: {"basic": 0.8, "intermediate": 0.2, "complex": 0.0} for cat in ["government", "transportation", "recreation"]}
            },
            "complex_scenarios": {
                "categories": ["business", "housing", "taxation"],
                "complexity_override": {cat: {"basic": 0.1, "intermediate": 0.4, "complex": 0.5} for cat in ["business", "housing", "taxation"]}
            }
        }
        
        config = focus_configs.get(focus_area, {})
        categories = config.get("categories", list(self.categories.keys())[:4])
        complexity_override = config.get("complexity_override", {})
        
        return self.generate_questions(
            num_questions=num_questions,
            categories=categories,
            complexity_override=complexity_override
        )

def main():
    generator = SimpleQuestionGenerator()
    
    print("Generating test questions for evaluation...")
    
    test_sets = {
        "comprehensive": generator.generate_questions(50),
        "basic_services": generator.generate_focused_test_set("basic_services", 30),
        "complex_scenarios": generator.generate_focused_test_set("complex_scenarios", 20)
    }
    
    for test_name, questions in test_sets.items():
        filename = generator.save_questions(questions, f"simple_{test_name}_questions.json")
        
        category_counts = {}
        complexity_counts = {}
        for q in questions:
            category_counts[q.category] = category_counts.get(q.category, 0) + 1
            complexity_counts[q.complexity] = complexity_counts.get(q.complexity, 0) + 1
        
        print(f"\n{test_name.upper()} TEST SET:")
        print(f"   File: {filename}")
        print(f"   Total questions: {len(questions)}")
        print(f"   Categories: {', '.join(f'{k}({v})' for k, v in category_counts.items())}")
        print(f"   Complexity: {', '.join(f'{k}({v})' for k, v in complexity_counts.items())}")
    
    print(f"\nGenerated {sum(len(qs) for qs in test_sets.values())} total questions across {len(test_sets)} test sets")

if __name__ == "__main__":
    main()