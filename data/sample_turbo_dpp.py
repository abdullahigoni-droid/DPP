DPP_DATA = {

    # ── SECTION 1: Identity & Provenance ──────────────────────────────────
    "dpp_id": "dpp_01KB0SM72CPK0RZHNCNDTMWZHB",   # ULID, generated at runtime
    "dpp_version": "1.0",
    "issued_date": "2025-06-12",
    # placeholder
    "passport_url": "https://abdullahigoni-droid.github.io/DPP/{dpp_id}",

    "original_core": {
        "oem_part_number": "49335-00850",
        "oem_manufacturer": "Mitsubishi Turbocharger & Engine Europe",
        "serial_number": "VW-CRF-2019-004821",
        "vehicle_fitment": {
            "make": "Volkswagen",
            "model": "Crafter",
            "engine_code": "CKTB",
            "year_range": "2017–2023",
            "displacement_cc": 1968,
            "power_kw": 103
        }
    },

    "remanufacturer": {
        "company_name": "TurboReman Ltd",
        "eoid": "GB-EOID-2024-TRL-00421",          # Economic Operator ID
        "facility_id": "FAC-BHAM-001",
        "facility_location": "Birmingham, UK",
        "facility_country_code": "GB"
    },

    "remanufactured_unit": {
        "tracking_id": "TRB-2024-00147",
        "data_carrier": "Laser-etched QR code on compressor housing",
        "reman_date": "2025-06-10",
        "product_name": "Remanufactured Variable Nozzle Turbine (VNT) Turbocharger",
        "product_category": "Turbocharger"
    },

    # ── SECTION 2: Remanufacturing Operations ─────────────────────────────
    "component_disposition": [
        {
            "sub_assembly": "Turbine Housing (Cast Iron)",
            "disposition": "Reused",
            "action_detail": "Ultrasonically cleaned, crack-tested, and surface-restored. All mating faces measured to OEM tolerance ±0.02mm.",
            "material": "Cast Iron GJL-250"
        },
        {
            "sub_assembly": "Compressor Cover (Aluminium)",
            "disposition": "Reconditioned",
            "action_detail": "CNC machined to restore bore geometry. Anodised finish reapplied.",
            "material": "Aluminium Alloy A380"
        },
        {
            "sub_assembly": "Compressor Wheel",
            "disposition": "Replaced — Upgraded",
            "action_detail": "Replaced with billet 2618-forged aluminium wheel. +7% flow improvement over OEM.",
            "material": "2618 Forged Aluminium"
        },
        {
            "sub_assembly": "CHRA (Centre Housing Rotating Assembly)",
            "disposition": "Replaced",
            "action_detail": "Full new CHRA installed. New journal bearings, thrust collar, oil deflector, and piston ring seals.",
            "material": "Steel / Bronze alloy bearings"
        },
        {
            "sub_assembly": "VNT Nozzle Ring & Actuator",
            "disposition": "Reconditioned",
            "action_detail": "Vanes de-carbonised, freedom-of-movement restored. Actuator rod re-calibrated to OEM displacement spec.",
            "material": "Stainless Steel"
        },
        {
            "sub_assembly": "Turbine Shaft & Wheel",
            "disposition": "Replaced",
            "action_detail": "New Inconel shaft-and-wheel assembly. Old shaft measured beyond wear limit (journal diameter < 11.94mm).",
            "material": "Inconel 713"
        }
    ],

    "testing_calibration": {
        "vsr_balancing": {
            "test_standard": "ISO 21940-11 Residual Unbalance",
            "test_speed_rpm": 180000,
            "balance_grade": "G0.4",
            "residual_unbalance_gmm": 0.12,
            "pass_threshold_gmm": 0.25,
            "result": "PASS",
            "test_date": "2025-06-10",
            "machine_id": "VSR-HOFMANN-03"
        },
        "actuator_calibration": {
            "type": "Pneumatic Wastegate / VNT",
            "set_pressure_mbar": 780,
            "rod_travel_mm": 1.85,
            "oem_spec_min_mm": 1.80,
            "oem_spec_max_mm": 1.90,
            "result": "PASS",
            "calibrated_by": "Technician ID: T-047"
        },
        "leak_test": {
            "test_pressure_bar": 1.5,
            "hold_time_seconds": 30,
            "result": "PASS"
        }
    },

    # ── SECTION 3: Sustainability & Environmental ─────────────────────────
    "sustainability": {
        "gwp_new_unit_kg_co2e": 47.2,
        "gwp_remanufactured_kg_co2e": 9.4,
        "gwp_saving_kg_co2e": 37.8,
        "gwp_saving_percent": 80.1,
        "gwp_methodology": "Based on ISO 14044 LCA boundary; cradle-to-gate. New unit benchmark: IHS Markit 2023 turbocharger LCA dataset.",
        "material_circularity": {
            "total_unit_weight_kg": 4.2,
            "reused_reconditioned_weight_kg": 2.94,
            "new_material_weight_kg": 1.26,
            "circularity_percent": 70.0
        },
        "energy_used_kwh": 3.8,
        "energy_source": "Grid + 40% on-site solar"
    },

    # ── SECTION 4: Commercial & Lifecycle ─────────────────────────────────
    "warranty": {
        "duration_months": 24,
        "mileage_limit_km": 100000,
        "conditions": "Warranty void if oil supply pipe not replaced at installation. Requires pre-lubrication on first start. Valid only with installation record.",
        "eu_regulation_reference": "EU 2023/1542 — Remanufactured goods warranty parity"
    },

    "installation_guidance": {
        "oil_priming": "Fill centre housing with clean engine oil before installation. Crank engine without starting for 10 seconds to prime oil feed.",
        "oil_feed_pipe": "MANDATORY: Replace oil feed pipe and banjo bolt. Do not reuse old pipe.",
        "torque_specs": [
            {"fastener": "Oil feed banjo bolt", "torque_nm": 22,
                "note": "New copper washers only"},
            {"fastener": "Turbine housing V-clamp", "torque_nm": 10,
                "note": "Tighten evenly in star pattern"},
            {"fastener": "Turbo mounting studs (M8)", "torque_nm": 28,
             "note": "Apply anti-seize compound"}
        ],
        "run_in_procedure": "Idle for 3 minutes on first start. Do not rev above 2,500 RPM for first 50km.",
        "technical_manual_url": "https://yourcompany.github.io/manuals/TRB-VW-CRAFTER-CKTB-v2.pdf"
    },

    "end_of_life": {
        "takeback_scheme": "TurboReman Core Return Programme",
        "instructions": "Contact returns@turboreman.co.uk with your unit serial number. A pre-paid collection label will be issued within 48 hours. Core must be drained of oil and sealed in original packaging.",
        "core_value_credit_gbp": 45.00,
        "hazardous_materials": "Engine oil residues — drain prior to return. Not WEEE-classified."
    }
}
