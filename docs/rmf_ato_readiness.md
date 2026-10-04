
# RMF/ATO Readiness Planning
## AI/ML Mission Request Classification Prototype

**Project:** AI/ML Mission Delivery Demonstration

**Status:** Educational prototype

**Operational status:** Not deployed

**Authorization status:** No Authority to Operate (ATO)

## 1. Purpose

This document illustrates how a Technical Project Manager
could incorporate federal cybersecurity authorization
considerations into an AI/ML delivery lifecycle.

It is a planning exercise, not an official RMF package,
security assessment, or authorization decision.

The project uses synthetic data and does not connect
to government systems.

## 2. RMF Overview

The NIST Risk Management Framework (RMF)
provides a structured approach for managing
security and privacy risks.

The seven RMF steps are:

1. Prepare
2. Categorize
3. Select
4. Implement
5. Assess
6. Authorize
7. Monitor

The exact requirements, responsibilities, and
approval processes depend on the sponsoring
organization and applicable federal policies.

## 3. RMF Planning Matrix

| RMF Step | Illustrative Activity | Potential Evidence | Proposed Responsible Role |
|---|---|---|---|
| Prepare | Identify stakeholders, mission objectives, and risk strategy | Stakeholder register, project charter | Program Manager |
| Categorize | Define system boundary and information types | Boundary diagram, impact analysis | System Owner / Security Lead |
| Select | Identify applicable security controls | Control baseline, tailoring decisions | Security Lead |
| Implement | Plan and implement selected controls | System Security Plan, configuration evidence | Engineering / Security Teams |
| Assess | Evaluate implemented controls | Security assessment results, findings | Independent Assessment Team |
| Authorize | Support risk acceptance decision | Authorization package, POA&M | Authorizing Official |
| Monitor | Track vulnerabilities, changes, and residual risks | Monitoring reports, remediation tracking | System Owner / Security Team |

These are illustrative responsibilities.
Actual assignments must follow organizational policy.

## 4. System Boundary Considerations

Before an operational implementation,
stakeholders would need to determine:

- Which components are within the authorization boundary?
- What information types would the system process?
- Would any information be classified or controlled?
- Which external systems would exchange data?
- Where would model training occur?
- Where would inference occur?
- Who would administer the environment?
- What logging and monitoring services would be used?
- Which shared or inherited controls might apply?

The current prototype has no established
federal authorization boundary.

## 5. AI/ML-Specific Security Considerations

Potential concerns include:

### Data Protection

- Data provenance and approved use
- Access controls for training datasets
- Sensitive information handling
- Retention and deletion requirements
- Data poisoning and integrity risks

### Model Protection

- Unauthorized model modification
- Model artifact integrity
- Software dependency vulnerabilities
- Controlled promotion of model versions
- Protection against untrusted serialized artifacts

### Inference Security

- Input validation
- Abuse and adversarial input handling
- Access control for prediction services
- Audit logging
- Human review of consequential decisions

### Operational Monitoring

- Model performance changes
- Security events
- Drift indicators
- Incident response
- Change and configuration management

These considerations would require
system-specific analysis and control selection.

## 6. AI Governance Considerations

A hypothetical operational program should
also consider:

- Defined model purpose and permitted uses
- Human oversight and accountability
- Representative evaluation data
- Model performance and error analysis
- Testing of unfamiliar inputs
- Model score calibration
- Documented limitations
- Stakeholder review and approval
- Ongoing monitoring and reassessment

The NIST AI Risk Management Framework
can provide complementary guidance.

AI governance review does not replace
required cybersecurity authorization.

## 7. Proposed Authorization Deliverables

Potential deliverables include:

| Deliverable | Purpose |
|---|---|
| System boundary diagram | Define included components and interfaces |
| Information impact analysis | Support system categorization |
| System Security Plan (SSP) | Document selected and implemented controls |
| Control implementation evidence | Support security assessment |
| Security Assessment Report (SAR) | Document assessment results |
| Plan of Action and Milestones (POA&M) | Track identified weaknesses |
| Continuous monitoring strategy | Define ongoing oversight |
| Incident response procedures | Support security event management |
| Configuration management plan | Control system changes |
| Authorization decision record | Document the authorized official's decision |

The required package may differ
by organization, system, and authorization path.

## 8. Illustrative Security Delivery Milestones

| Milestone | Proposed Timing | Dependency |
|---|---|---|
| Identify security stakeholders | Project initiation | Mission sponsorship |
| Establish preliminary system boundary | Requirements phase | Architecture definition |
| Determine categorization requirements | Early design | Information type analysis |
| Identify control baseline | Design phase | Categorization |
| Implement and document controls | Development | Approved architecture |
| Conduct security assessment | Pre-release | Implemented controls |
| Address assessment findings | Pre-authorization | Assessment results |
| Support authorization decision | Before operational use | Completed required evidence |
| Begin continuous monitoring | After authorization, as applicable | Approved monitoring approach |

Timing is illustrative, not an approved
government project schedule.

## 9. Integration With Agile Delivery

Security work should be represented
in the product backlog and delivery plan.

Examples include:

- Security architecture reviews
- Identity and access requirements
- Logging and audit requirements
- Vulnerability remediation
- Dependency scanning
- Security test evidence
- Documentation updates
- Authorization-related milestones

The Technical Project Manager should
track these items alongside functional
requirements, risks, and integration dependencies.

## 10. Risk and Dependency Management

The project risk register includes
security and authorization-related risks.

Relevant examples:

- R-05: Unauthorized sensitive data exposure
- R-07: Inadequate testing
- R-09: Late security authorization planning
- R-10: Integration and schedule dependencies

These risks should be reviewed during
regular project governance activities.

## 11. Current Prototype Readiness Assessment

| Capability | Current Status |
|---|---|
| Synthetic dataset | Implemented |
| Baseline ML training | Implemented |
| Standalone prediction logic | Implemented |
| Human-review decision indicator | Implemented |
| Automated software tests | 8 passed |
| Model card | Documented |
| Risk register | Documented |
| Reference architecture | Documented |
| Federal system categorization | Not performed |
| Security control implementation | Not established |
| Independent security assessment | Not performed |
| Formal authorization package | Not created |
| ATO | Not obtained |
| Operational deployment | Not performed |

## 12. Technical Project Manager Responsibilities

For a hypothetical federal AI/ML program,
a Technical Project Manager could:

1. Coordinate security and engineering stakeholders.
2. Integrate authorization milestones into the schedule.
3. Track control implementation dependencies.
4. Maintain visibility into assessment findings.
5. Coordinate remediation and POA&M tracking.
6. Escalate security risks affecting delivery.
7. Support release-readiness reviews.
8. Ensure operational deployment is not represented
   as authorized without the required decision.

The Technical Project Manager supports
these activities but does not independently
grant an ATO.

## 13. Conclusion

This document demonstrates an approach
to planning RMF-related activities for
a hypothetical AI/ML delivery program.

The current project remains an educational
prototype using synthetic data.

It has not undergone federal security
authorization and must not be represented
as an operationally approved system.
