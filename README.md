# Stripe Secret Key Validator Tool

## Overview

The **Stripe Secret Key Validator Tool** is a Python-based command-line utility designed to verify the validity and permissions of Stripe secret keys (sk keys). The tool performs multiple checks against various Stripe API endpoints to ensure the key is functional and has access to essential resources.

## Features

- **Key Type Detection**: Automatically identifies whether the provided key is a live key (`sk_live_...`) or a test key (`sk_test_...`).
- **Real-Time API Checks**: Verifies access to critical Stripe resources, including Charges, Customers, Refunds, Balance, Payment Intents, Cards, and Disputes.
- **Color-Coded Output**: Provides visual feedback with green tick marks (`✓`) for successful verifications and red cross marks (`✗`) for failed ones.
- **Logging**: Records all checks performed, including results and timestamps, in a log file (`stripe_key_check.log`).
- **Summary Report**: Generates a summary of the total checks, passed checks, and failed checks for quick review.
- **Error Categorization**: Differentiates between unauthorized, forbidden, and other errors to give detailed diagnostic information.
<img src="https://raw.githubusercontent.com/yaratul/discord/main/images%20(7).jpeg" alt="https://t.me/notnxboi">

## Prerequisites

Make sure you have Python 3 installed on your system. Additionally, you'll need to install the required Python packages:

```bash
pip install requests colorama
