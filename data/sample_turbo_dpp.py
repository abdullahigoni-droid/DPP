DPP_DATA = {
    "dpp_id": "dpp_01KTTG4PV63D5D8JB7M2VNT001",
    "dpp_version": "2.0",
    "issued_date": "2026-05-21",
    "passport_url": "https://abdullahigoni-droid.github.io/DPP/{dpp_id}",

    "product": {
        "name": "Remanufactured Variable Nozzle Turbocharger",
        "brand": "The Turbo Guy",
        "model": "49335-00850 VNT Reman",
        "category": "Turbocharger",
        "status": "Remanufactured and Bench Tested",
        "condition": "Trade-ready remanufactured unit",
        "collection": "Turbo Guy Remanufactured Turbo Programme",
        "description": (
            "A professionally remanufactured variable nozzle turbocharger prepared for UK trade "
            "supply. The unit is dismantled, cleaned, inspected, rebuilt with service-critical "
            "components, balanced, calibrated, and recorded in this Digital Product Passport."
        ),
        "weight_kg": 4.2,
        "country_of_origin": "GB",
        "image_path": "download.jpeg",
    },

    "original_core": {
        "oem_part_number": "49335-00850",
        "oem_manufacturer": "Mitsubishi Turbocharger & Engine Europe",
        "serial_number": "VW-CRF-2019-004821",
        "vehicle_fitment": {
            "make": "Volkswagen",
            "model": "Crafter",
            "engine_code": "CKTB",
            "year_range": "2017-2023",
            "displacement_cc": 1968,
            "power_kw": 103,
        },
    },

    "remanufacturer": {
        "company_name": "The Turbo Guy",
        "eoid": "Internal operator reference: TTG-GLA-001",
        "facility_id": "TTG-GLA-RENFREW",
        "facility_location": "337 Renfrew Road, Glasgow, G51 4SP",
        "facility_country_code": "GB",
        "website": "https://www.theturboguy.com/",
        "phone": "0141 649 9426",
        "email": "sales@theturboguy.com",
        "trade_note": "Trade-only supplier serving businesses UK wide",
    },

    "remanufactured_unit": {
        "tracking_id": "TTG-TRB-2026-00147",
        "data_carrier": "QR code linked to the digital passport",
        "reman_date": "2026-05-21",
        "product_name": "Remanufactured Variable Nozzle Turbocharger",
        "product_category": "Turbocharger",
        "gtin": "05060999123463",
        "serial_number": "TTG-VNT-2026-00147",
    },

    "card_summaries": [
        {
            "id": "overview",
            "title": "Product Overview",
            "description": "Essential turbocharger identity, fitment, and passport data",
            "count": 9,
        },
        {
            "id": "sustainability",
            "title": "Environmental Impact",
            "description": "Carbon, water, circularity, and remanufacturing benefits",
            "count": 5,
        },
        {
            "id": "materials",
            "title": "Materials & Traceability",
            "description": "Material split, reused content, and component traceability",
            "count": 6,
        },
        {
            "id": "journey",
            "title": "Product Journey",
            "description": "Core receipt through test, dispatch, and return loop",
            "count": 6,
        },
        {
            "id": "remanufacturing",
            "title": "Remanufacturing",
            "description": "Inspection, cleaning, rebuild, calibration, and QA steps",
            "count": 8,
        },
        {
            "id": "lifecycle",
            "title": "Lifecycle",
            "description": "Warranty, installation, support, and end-of-life guidance",
            "count": 7,
        },
    ],

    "aboutThisDPP": {
        "title": "What is a Digital Product Passport?",
        "description": (
            "This passport provides a verified digital record for the turbocharger, covering "
            "identity, provenance, component disposition, remanufacturing operations, testing, "
            "environmental impact, installation requirements, and end-of-life options."
        ),
        "whatYouCanSee": [
            "Original core and vehicle fitment information",
            "Remanufacturing and component disposition records",
            "Bench test, balancing, calibration, and leak-test results",
            "Material reuse, circularity, and estimated carbon impact",
            "Installation, warranty, support, and core-return instructions",
        ],
        "whyItMatters": [
            "Helps trade customers verify the unit and installation requirements",
            "Supports repair, reuse, remanufacturing, and core return workflows",
            "Keeps product data available from first scan through end of life",
        ],
    },

    "component_disposition": [
        {
            "sub_assembly": "Turbine Housing (Cast Iron)",
            "disposition": "Reused",
            "action_detail": "Ultrasonically cleaned, crack-tested, and surface restored. Mating faces measured to OEM tolerance.",
            "material": "Cast Iron GJL-250",
        },
        {
            "sub_assembly": "Compressor Cover (Aluminium)",
            "disposition": "Reconditioned",
            "action_detail": "Cleaned, inspected, machined where required, and pressure checked before rebuild.",
            "material": "Aluminium Alloy A380",
        },
        {
            "sub_assembly": "Compressor Wheel",
            "disposition": "Replaced - Upgraded",
            "action_detail": "Replaced with billet 2618-forged aluminium wheel to restore flow performance.",
            "material": "2618 Forged Aluminium",
        },
        {
            "sub_assembly": "CHRA (Centre Housing Rotating Assembly)",
            "disposition": "Replaced",
            "action_detail": "New CHRA installed with new journal bearings, thrust collar, oil deflector, and piston ring seals.",
            "material": "Steel / Bronze alloy bearings",
        },
        {
            "sub_assembly": "VNT Nozzle Ring and Actuator",
            "disposition": "Reconditioned",
            "action_detail": "Vanes de-carbonised and actuator rod calibrated to OEM displacement range.",
            "material": "Stainless Steel",
        },
        {
            "sub_assembly": "Turbine Shaft and Wheel",
            "disposition": "Replaced",
            "action_detail": "New Inconel shaft-and-wheel assembly fitted after original shaft exceeded wear limit.",
            "material": "Inconel 713",
        },
    ],

    "testing_calibration": {
        "vsr_balancing": {
            "test_standard": "ISO 21940-11 residual unbalance",
            "test_speed_rpm": 180000,
            "balance_grade": "G0.4",
            "residual_unbalance_gmm": 0.12,
            "pass_threshold_gmm": 0.25,
            "result": "PASS",
            "test_date": "2026-05-21",
            "machine_id": "TTG-VSR-GLA-03",
        },
        "actuator_calibration": {
            "type": "Pneumatic VNT actuator",
            "set_pressure_mbar": 780,
            "rod_travel_mm": 1.85,
            "oem_spec_min_mm": 1.80,
            "oem_spec_max_mm": 1.90,
            "result": "PASS",
            "calibrated_by": "The Turbo Guy QA bench",
        },
        "leak_test": {
            "test_pressure_bar": 1.5,
            "hold_time_seconds": 30,
            "result": "PASS",
        },
    },

    "regulatory": {
        "materials": {
            "reusedContent": 70,
            "recycledContent": 0,
            "virginContent": 30,
            "materialComposition": [
                {"material": "Reused cast iron housing", "percentage": 42, "status": "Reused"},
                {"material": "Reconditioned aluminium cover", "percentage": 18, "status": "Reconditioned"},
                {"material": "New rotating assembly and bearings", "percentage": 25, "status": "Replaced"},
                {"material": "Seals, fasteners, and calibration parts", "percentage": 15, "status": "Replaced"},
            ],
        },
        "carbonFootprint": 9.4,
        "waterFootprint": 4.1,
        "energyConsumption": 3.8,
        "recyclability": 95,
        "compliance": {
            "certifications": [
                {"name": "Bench Tested", "year": "2026"},
                {"name": "VSR Balanced", "year": "2026"},
                {"name": "DPP Demonstrator", "year": "2026"},
            ],
            "standards": ["ISO 21940-11 balancing reference", "ESPR-aligned DPP data structure"],
        },
        "endOfLife": {
            "takeBackProgram": True,
            "recyclability": 95,
            "instructions": (
                "Return spent or failed turbo cores to The Turbo Guy for inspection, reuse, "
                "remanufacturing, or material recovery. Drain oil residues before transport."
            ),
            "programDetails": (
                "Core eligibility and value are confirmed after inspection. Units with no resale "
                "or remanufacturing value can be recycled or returned subject to carriage terms."
            ),
        },
    },

    "sustainability": {
        "circularScore": 82,
        "gwp_new_unit_kg_co2e": 47.2,
        "gwp_remanufactured_kg_co2e": 9.4,
        "gwp_saving_kg_co2e": 37.8,
        "gwp_saving_percent": 80.1,
        "gwp_methodology": (
            "Illustrative cradle-to-gate comparison for a remanufactured turbocharger, "
            "aligned to ISO 14040/14044 LCA principles."
        ),
        "material_circularity": {
            "total_unit_weight_kg": 4.2,
            "reused_reconditioned_weight_kg": 2.94,
            "new_material_weight_kg": 1.26,
            "circularity_percent": 70.0,
        },
        "energy_used_kwh": 3.8,
        "energy_source": "Grid electricity with reusable cleaning media",
        "carbonComparison": {
            "current": {"value": 9.4, "unit": "kg CO2e", "label": "This Reman Unit"},
            "baseline": {"value": 47.2, "unit": "kg CO2e", "label": "New Turbocharger"},
            "savings": {"value": 37.8, "unit": "kg CO2e", "percentage": 80.1},
        },
        "impactMetrics": [
            {"label": "Carbon Footprint", "value": 9.4, "unit": "kg CO2e", "grade": "A", "context": "Remanufactured unit"},
            {"label": "Carbon Saved", "value": 37.8, "unit": "kg CO2e", "grade": "A+", "context": "Compared with new"},
            {"label": "Circularity", "value": 70, "unit": "%", "grade": "A", "context": "Reused/reconditioned mass"},
            {"label": "Recyclability", "value": 95, "unit": "%", "grade": "A+", "context": "Metal-heavy assembly"},
        ],
        "achievements": [
            "Existing turbo core diverted into a remanufacturing loop",
            "Major housings reused or reconditioned",
            "Service-critical rotating components replaced and verified",
            "Core return supports repeat remanufacturing and metal recovery",
        ],
    },

    "lca": {
        "scope": "Cradle-to-gate remanufacturing estimate",
        "functionalUnit": "One remanufactured VNT turbocharger",
        "methodology": "Screening LCA using mass balance, energy use, and new-unit benchmark factors.",
        "totalCarbonFootprint": 9.4,
        "carbonBreakdown": [
            {"stage": "Core cleaning and inspection", "value": 1.5, "unit": "kg CO2e", "percentage": 16},
            {"stage": "Replacement components", "value": 4.4, "unit": "kg CO2e", "percentage": 47},
            {"stage": "Machining, balancing, calibration", "value": 2.1, "unit": "kg CO2e", "percentage": 22},
            {"stage": "Packaging and UK trade distribution", "value": 1.4, "unit": "kg CO2e", "percentage": 15},
        ],
    },

    "materialSpecifications": {
        "type": "Cast iron, aluminium, Inconel, steel, bronze, and elastomer seals",
        "manufacturer": "Mixed OEM-equivalent and approved replacement components",
        "keyMaterials": [
            {"name": "Cast Iron GJL-250", "application": "Turbine housing", "status": "Reused"},
            {"name": "Aluminium Alloy A380", "application": "Compressor cover", "status": "Reconditioned"},
            {"name": "Inconel 713", "application": "Turbine shaft and wheel", "status": "Replaced"},
            {"name": "Steel / bronze alloys", "application": "CHRA and bearings", "status": "Replaced"},
        ],
    },

    "materialOrigins": {
        "materials": [
            {
                "name": "Returned turbo core",
                "supplier": "UK trade customer core return",
                "origin": "United Kingdom",
                "percentage": 70,
                "details": "Major housings retained after inspection and cleaning.",
            },
            {
                "name": "Replacement service kit",
                "supplier": "Approved aftermarket / OEM-equivalent supply",
                "origin": "Mixed",
                "percentage": 30,
                "details": "Rotating assembly, bearings, seals, fasteners, and calibration parts.",
            },
        ],
    },

    "supplyChain": {
        "journey": [
            {
                "date": "May 2026",
                "title": "Core Received",
                "facility": "The Turbo Guy",
                "location": "Glasgow, Scotland",
                "description": "Returned turbo core logged, visually inspected, and matched to OEM part number.",
            },
            {
                "date": "May 2026",
                "title": "Strip, Clean, and Inspect",
                "facility": "The Turbo Guy workshop",
                "location": "337 Renfrew Road, Glasgow",
                "description": "Unit dismantled, cleaned, measured, and assessed for reuse, reconditioning, or replacement.",
            },
            {
                "date": "May 2026",
                "title": "Rebuild",
                "facility": "The Turbo Guy workshop",
                "location": "Glasgow, Scotland",
                "description": "Accepted housings rebuilt with replacement CHRA, shaft, seals, and calibrated actuator components.",
            },
            {
                "date": "May 2026",
                "title": "Bench Test and Calibration",
                "facility": "The Turbo Guy QA bench",
                "location": "Glasgow, Scotland",
                "description": "VSR balancing, actuator calibration, and pressure leak test recorded before release.",
            },
            {
                "date": "May 2026",
                "title": "Trade Dispatch",
                "facility": "The Turbo Guy dispatch",
                "location": "UK wide",
                "description": "Finished unit supplied to a trade customer with installation and core-return requirements.",
            },
        ],
    },

    "manufacturing": {
        "date": "2026-05-21",
        "facility": "The Turbo Guy",
        "location": "Glasgow, Scotland",
        "process": "Turbocharger remanufacturing",
        "equipment": "Parts washer, inspection tools, balancing rig, actuator calibration bench, leak-test rig",
        "qualityControl": "Visual inspection, dimensional checks, VSR balancing, actuator calibration, and pressure leak testing",
    },

    "remanufacturing": {
        "processor": "The Turbo Guy",
        "location": "Glasgow, Scotland",
        "date": "2026-05-21",
        "condition": "Remanufactured - tested and ready for trade supply",
        "certification": "The Turbo Guy remanufacturing QA record",
        "warranty": "Commercial warranty subject to installation and returns requirements",
        "processes": [
            "Core identification and serial traceability",
            "Full strip-down and ultrasonic cleaning",
            "Crack check and dimensional inspection of reusable housings",
            "Replacement of CHRA, shaft/wheel, bearings, seals, and fasteners where required",
            "VNT vane cleaning and actuator calibration",
            "VSR balancing at high speed",
            "Pressure leak testing",
            "Final inspection, DPP record update, and trade dispatch",
        ],
    },

    "warranty": {
        "duration_months": 12,
        "mileage_limit_km": 100000,
        "coverage": "Commercial warranty subject to The Turbo Guy sale, returns, and installation requirements.",
        "conditions": (
            "Warranty support requires correct installation, oil feed inspection/replacement where required, "
            "pre-lubrication, and an installation record. Oil starvation, contamination, and foreign object "
            "damage are excluded."
        ),
        "eu_regulation_reference": "ESPR-aligned remanufactured product data record",
        "highlights": [
            {"label": "Bench tested", "value": "PASS", "subtitle": "Calibration and leak test"},
            {"label": "Warranty", "value": "12 mo", "subtitle": "Subject to terms"},
            {"label": "Core loop", "value": "Return", "subtitle": "Inspection-based credit"},
        ],
    },

    "installation_guidance": {
        "oil_priming": "Fill centre housing with clean engine oil before installation and crank without starting to prime oil feed.",
        "oil_feed_pipe": "Replace or verify the oil feed pipe and banjo bolt before fitment. Do not install onto a contaminated oil system.",
        "torque_specs": [
            {"fastener": "Oil feed banjo bolt", "torque_nm": 22, "note": "Use new copper washers"},
            {"fastener": "Turbine housing V-clamp", "torque_nm": 10, "note": "Tighten evenly"},
            {"fastener": "Turbo mounting studs (M8)", "torque_nm": 28, "note": "Apply anti-seize compound"},
        ],
        "run_in_procedure": "Idle for 3 minutes on first start. Avoid high boost and engine speeds above 2,500 RPM for the first 50 km.",
        "technical_manual_url": "https://www.theturboguy.com/tech-support/",
    },

    "careInstructions": {
        "primary": "Installation quality is critical to turbocharger life.",
        "handling": [
            "Keep oil galleries capped until installation",
            "Do not rotate the actuator rod without calibration reference",
            "Keep foreign objects away from turbine and compressor openings",
        ],
        "warnings": [
            "Do not fit before resolving oil starvation or boost-control faults",
            "Do not reuse contaminated oil feed lines",
            "Do not run the engine immediately after fitment without oil priming",
        ],
    },

    "end_of_life": {
        "takeback_scheme": "The Turbo Guy core return and cash-for-core inspection process",
        "instructions": (
            "Email The Turbo Guy with turbo part numbers, OE references, and photos. "
            "Drain oil and package the core securely before return."
        ),
        "core_value_credit_gbp": 45.00,
        "hazardous_materials": "Engine oil residues - drain before return. Not WEEE-classified.",
    },

    "impactEquivalencies": {
        "metrics": [
            {
                "metric": "carbon",
                "value": 37.8,
                "unit": "kg CO2e",
                "equivalencies": [
                    {"label": "Passenger car driving avoided", "value": 139, "unit": "km"},
                    {"label": "Smartphone charges", "value": 3828, "unit": "charges"},
                ],
            }
        ],
    },

    "support": {
        "customerService": "The Turbo Guy trade support",
        "phone": "0141 649 9426",
        "email": "sales@theturboguy.com",
        "website": "https://www.theturboguy.com/",
        "address": "337 Renfrew Road, Glasgow, G51 4SP",
    },
}
