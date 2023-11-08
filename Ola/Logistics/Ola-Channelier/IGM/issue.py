{
  "context": {
    "bap_id": "integrations-preprod.channelier.com",
    "bap_uri": "https://integrations-preprod.channelier.com/ondc",
    "domain": "nic2004:60232",
    "core_version": "1.0.0",
    "ttl": "PT30S",
    "bpp_id": "ondc-preprod-lsp.olacabs.com",
    "bpp_uri": "https://ondc-preprod-lsp.olacabs.com",
    "transaction_id": "cdba61e8-6ef0-4c2a-8105-e7871f18f6b3",
    "message_id": "aa3903a2-bbf1-4cde-b46e-370fb715ddec",
    "country": "IND",
    "city": "std:080",
    "timestamp": "2023-10-19T10:14:27.381Z",
    "action": "issue"
  },
  "message": {
    "issue": {
      "id": "c4887d8a-ec99-4706-b835-b24bec09369e",
      "category": "FULFILLMENT",
      "sub_category": "FLM02",
      "complainant_info": {
        "person": {
          "name": "Koramangala"
        },
        "contact": {
          "phone": "9900163002",
          "email": "mahesh.herle@olacabs.com"
        }
      },
      "order_details": {
        "id": "2023-10-18-781782",
        "state": "Completed",
        "items": [
          {
            "id": "CU14I0",
            "quantity": 2
          }
        ],
        "fulfillments": [
          {
            "id": "L-F-1697653813857",
            "state": "Pending"
          }
        ],
        "provider_id": "CU14"
      },
      "description": {
        "short_desc": "Still not received",
        "long_desc": "Still not received",
        "additional_desc": {
          "url": "https://buyerapp.com/additonal-details/desc.txt",
          "content_type": "text/plain"
        },
        "images": []
      },
      "source": {
        "network_participant_id": "buyer-app-preprod.ondc.org",
        "type": "CONSUMER"
      },
      "expected_response_time": {
        "duration": "PT1H"
      },
      "expected_resolution_time": {
        "duration": "P1D"
      },
      "status": "OPEN",
      "issue_type": "ISSUE",
      "issue_actions": {
        "complainant_actions": [
          {
            "complainant_action": "OPEN",
            "short_desc": "Complaint created",
            "updated_at": "2023-10-19T10:14:27.325Z",
            "updated_by": {
              "org": {
                "name": "buyer-app-preprod.ondc.org::nic2004:52110"
              },
              "contact": {
                "phone": "6239083807",
                "email": "Rishabhnand.singh@ondc.org"
              },
              "person": {
                "name": "Rishabhnand Singh"
              }
            }
          }
        ],
        "respondent_actions": [
          {
            "respondent_action": "PROCESSING",
            "short_desc": "Complaint is being processed",
            "updated_by": {
              "org": {
                "name": "integrations-preprod.channelier.com::nic2004:52110"
              },
              "contact": {
                "phone": "9999999999",
                "email": "respondent@channelier.com"
              },
              "person": {
                "name": "John discovery"
              }
            },
            "cascaded_level": 1,
            "updated_at": "2023-10-19T10:14:27.376Z"
          },
          {
            "respondent_action": "CASCADED",
            "short_desc": "Complaint cascaded to transaction counterparty",
            "updated_by": {
              "org": {
                "name": "integrations-preprod.channelier.com::nic2004:60232"
              },
              "contact": {
                "phone": "9999999999",
                "email": "respondent@channelier.com"
              },
              "person": {
                "name": "John discovery"
              }
            },
            "cascaded_level": 2,
            "updated_at": "2023-10-19T10:14:27.381Z"
          }
        ]
      },
      "created_at": "2023-10-19T10:14:27.122Z",
      "updated_at": "2023-10-19T10:14:27.122Z"
    }
  }
}