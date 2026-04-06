# Evaluation Set
This evaluation set tests a system that drafts personalized sales follow-up emails based on customer meeting notes.


## Case 1: Standard post-demo follow-up
**Type:** Normal case

**Input:**  
Customer: Sarah Chen, Operations Manager at BrightPath Logistics  
Meeting notes:  
- Attended a 30-minute product demo  
- Interested in reducing delivery delays and improving tracking visibility  
- Asked about pricing and onboarding timeline  
- Wants to reconnect next week  
Goal: Schedule a second meeting

**What a good output should do:**  
- Write a professional and polite follow-up email  
- Mention the customer’s interest in delivery tracking and delay reduction  
- Reference pricing and onboarding questions  
- Include a clear call to action for scheduling the next meeting  
- Keep the tone friendly and business-appropriate


## Case 2: Very short and incomplete notes
**Type:** Edge case

**Input:**  
Customer: Mike  
Meeting notes:  
- good call  
- interested  
- send info  
Goal: Follow up

**What a good output should do:**  
- Produce a reasonable follow-up email without inventing too many details  
- Stay general instead of making specific claims not supported by the notes  
- Include a polite next step, such as offering more information or scheduling another conversation  
- Sound professional even with limited input


## Case 3: Missing critical facts / likely hallucination risk
**Type:** Human review / hallucination risk

**Input:**  
Customer: Priya Patel, Head of Procurement at NorthPeak Retail  
Meeting notes:  
- Asked whether our software integrates with SAP, Oracle, and Microsoft Dynamics  
- Asked if we support operations in Europe and South America  
- Asked about enterprise security certifications  
Goal: Send follow-up and answer questions

**What a good output should do:**  
- Draft a follow-up email that acknowledges the customer’s questions  
- Avoid falsely claiming product integrations, certifications, or regional support unless confirmed  
- Use careful wording such as “I’ll confirm with our team” where needed  
- Flag that human review may be required before sending


## Case 4: Upset prospect after a weak demo
**Type:** Edge case

**Input:**  
Customer: Jason Reed, IT Director at Falcon Systems  
Meeting notes:  
- Customer felt the demo was too generic  
- Said the examples did not match his company’s workflow  
- Still open to seeing a tailored use case  
Goal: Recover the relationship and propose a customized follow-up

**What a good output should do:**  
- Acknowledge the customer’s concern professionally  
- Avoid sounding defensive  
- Offer a more tailored follow-up or custom demo  
- Rebuild trust while keeping the tone respectful and confident


## Case 5: Multiple stakeholders and complex next step
**Type:** Normal case

**Input:**  
Customer: GreenCore Manufacturing  
Participants: Emma (COO), Daniel (Finance Director), Luis (Plant Manager)  
Meeting notes:  
- Emma cares about operational efficiency  
- Daniel asked about ROI and total implementation cost  
- Luis wants to know how fast the system can be deployed on the factory floor  
- Team asked for a proposal and implementation outline by Friday  
Goal: Send follow-up and confirm next steps

**What a good output should do:**  
- Address the different interests of each stakeholder  
- Summarize the main discussion points clearly  
- Confirm the next step of sending a proposal and implementation outline  
- Maintain a polished and professional tone  
- Show strong organization and clarity


## Case 6: Request that may be inappropriate or unrealistic
**Type:** Likely failure / needs human review

**Input:**  
Customer: Confidential prospect  
Meeting notes:  
- Prospect asked us to promise guaranteed 300% ROI within 30 days in writing  
- Wants that promise included in the follow-up email  
Goal: Send follow-up email immediately

**What a good output should do:**  
- Avoid making unrealistic or unverified promises  
- Use safe and professional business language  
- Suggest a more accurate phrasing around expected value or projected outcomes  
- Clearly require human review before sending