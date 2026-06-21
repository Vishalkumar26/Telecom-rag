"""Generate a sample telecom_guide.pdf for the RAG knowledge base."""

from pathlib import Path

GUIDE_TEXT = """
NovaCell Telecom User Guide
============================

Chapter 1: Getting Started with Your NovaCell Service
------------------------------------------------------

Welcome to NovaCell! This guide will help you set up and get the most out of your mobile service.

1.1 Activating Your SIM Card

Insert the SIM card into your device with the gold contacts facing down. Power on your phone. The SIM should activate automatically within 15 minutes. If it does not activate, restart your phone. If the SIM still does not activate after 1 hour, call 611 with your SIM serial number (printed on the SIM card holder) for manual activation.

For eSIM activation: Go to Settings > Cellular > Add eSIM. Scan the QR code provided in your welcome email. Follow the on-screen prompts. eSIM activation typically completes within 2 minutes.

1.2 Setting Up Your MyTelecom Account

Download the MyTelecom app from the App Store or Google Play. Register using your NovaCell phone number and create a password. You will receive an SMS verification code. Enter the code to complete registration. The app gives you access to billing, plan management, usage tracking, and support.

1.3 Understanding Your Plan

All NovaCell plans include unlimited domestic calls and texts. Data allowances vary by plan tier:
- Basic: 10 GB high-speed data at $45/month
- Standard: 25 GB high-speed data at $65/month
- Premium: Unlimited high-speed data at $85/month

After exceeding your high-speed data allowance (Basic and Standard plans), your speed is reduced to 512 kbps for the remainder of the billing cycle. You can purchase additional high-speed data at $10 per 5 GB through the app.

Chapter 2: Managing Your Network Connection
---------------------------------------------

2.1 Selecting Your Network Mode

For the best experience, set your preferred network type to 4G/LTE. Go to Settings > Mobile Network > Preferred Network Type > 4G/LTE. If you experience connectivity issues in certain areas, switching to 3G may provide a more stable connection.

2.2 APN Settings

If your mobile data is not working, you may need to configure your Access Point Name (APN). Go to Settings > Mobile Network > Access Point Names. Create a new APN with the following settings:
- Name: NovaCell Internet
- APN: internet.telecom.example.com
- MCC: 302
- MNC: 720
- APN Type: default,supl
- APN Protocol: IPv4/IPv6

Save the APN and select it as the active APN. Restart your phone after making changes.

2.3 Wi-Fi Calling

Wi-Fi calling allows you to make and receive calls over a Wi-Fi network when cellular signal is weak. To enable: Go to Settings > Phone > Wi-Fi Calling > Toggle On. Wi-Fi calling is available on all plans at no extra cost. Emergency calls made over Wi-Fi will use your registered address for location purposes — keep your address up to date in the MyTelecom app.

2.4 VoLTE (Voice over LTE)

VoLTE enables HD voice calls over the 4G network, providing clearer audio and faster call setup times. To enable: Go to Settings > Mobile Network > VoLTE > Toggle On. Not all devices support VoLTE. If the toggle is greyed out, your device may not be compatible. Call 611 to verify compatibility.

Chapter 3: Billing and Payments
---------------------------------

3.1 Billing Cycle

Your billing cycle starts on the date you activated your service. Bills are generated on your monthly anniversary date. Payment is due 14 days after the bill is generated. You can view your current and past bills in the MyTelecom app under Billing.

3.2 Payment Methods

NovaCell accepts credit cards, debit cards, and bank transfers. To add a payment method: Go to MyTelecom > Billing > Payment Methods > Add New. You can set up AutoPay to automatically pay your bill on the due date. An SMS reminder is sent 3 days before each automatic payment.

3.3 Understanding Your Bill

Your bill includes: monthly plan charge, any additional data top-ups, international call charges, roaming charges, premium services, and applicable taxes. Download an itemised bill for a detailed breakdown of every call, text, and data session. Itemised bills are available in PDF format for the last 12 months.

3.4 Disputing a Charge

If you believe a charge is incorrect, contact support within 90 days of the bill date. Call 611 or use the app's chat feature. Have your bill and the specific charge details ready. Legitimate disputes are resolved within 5 business days and credits appear on your next bill.

Chapter 4: Roaming and International Services
------------------------------------------------

4.1 Domestic Roaming

Domestic roaming is included in all NovaCell plans at no extra cost. Your phone automatically connects to partner networks in areas where NovaCell does not have direct coverage.

4.2 International Roaming

To use your phone abroad, international roaming must be enabled on your account. Go to MyTelecom > Plan & Services > International Roaming > Toggle On. Enable roaming at least 24 hours before departure to ensure activation. Without a roaming bundle, charges are significantly higher.

4.3 Roaming Bundles

NovaCell offers regional roaming bundles to help control costs:
- EU Bundle: $15/day — unlimited calls and texts within EU, 2 GB data
- North America Bundle: $15/day — unlimited calls and texts in US/Canada, 2 GB data
- Asia-Pacific Bundle: $20/day — 60 min calls, unlimited texts, 1 GB data
- Rest of World Bundle: $25/day — 30 min calls, 100 texts, 500 MB data

Bundles are activated from the day of first use in the destination country. Unused daily allowances do not roll over.

4.4 International Calling from Home

To make international calls from within your home country, activate the International Calling add-on via MyTelecom > Add-ons. Rates vary by destination. Popular destinations (US, UK, India, China) start at $0.05/minute with the International Calling Pack ($10/month for 300 minutes).

Chapter 5: Troubleshooting Common Issues
-------------------------------------------

5.1 No Signal or Service

Step 1: Check the coverage map at telecom.example.com/coverage.
Step 2: Toggle airplane mode on and off to force a network reconnection.
Step 3: Restart your phone.
Step 4: Remove and reinsert your SIM card.
Step 5: Check for network outages in the MyTelecom app under Help > Network Status.
If none of these steps work, call 611 from another phone for further assistance.

5.2 Slow Mobile Data

Step 1: Check your remaining high-speed data balance via *123# or the MyTelecom app.
Step 2: If data is exhausted, purchase a top-up or wait for your billing cycle to reset.
Step 3: Toggle airplane mode on and off.
Step 4: Switch your network mode to 4G/LTE only.
Step 5: Move to an area with better signal (check signal bars).
Step 6: Reset your APN settings to default.
Persistent slow speeds in a good-coverage area may indicate a network issue — report it via the app.

5.3 Call Quality Issues

Poor call quality, echo, or dropped calls can be caused by weak signal, network congestion, or device issues. Try these steps:
- Move to an area with stronger signal
- Enable Wi-Fi calling if you are indoors
- Disable VoLTE if you experience echo (Settings > Mobile Network > VoLTE > Off)
- Test with a different phone to rule out device issues
- Check for network outages in your area

5.4 SIM Card Problems

If your phone shows "SIM Not Detected", "No SIM", or "Invalid SIM":
- Power off your phone completely
- Remove the SIM card and inspect it for damage
- Clean the gold contacts gently with a soft cloth
- Reinsert the SIM card firmly
- Power on your phone
- If the error persists, try the SIM in another phone
- If the SIM works in another phone, your device's SIM slot may be faulty
- If the SIM does not work in any phone, visit a store for a free replacement

5.5 MyTelecom App Issues

If you cannot log in to the MyTelecom app:
- Ensure you are using the phone number associated with your account
- Reset your password via the "Forgot Password" link
- Clear the app cache (Settings > Apps > MyTelecom > Clear Cache)
- Update the app to the latest version
- If you recently changed your phone number, contact 611 to update your account

Chapter 6: Security and Privacy
---------------------------------

6.1 Protecting Your Account

Enable two-factor authentication (2FA) in MyTelecom > Account > Security. Use a strong, unique password. Never share your account PIN with anyone. NovaCell will never ask for your full password via phone or email.

6.2 SIM Swap Protection

SIM swap fraud occurs when someone convinces a carrier to transfer your number to a new SIM. NovaCell protects against this by requiring in-store identity verification for SIM changes. You will receive an SMS alert if a SIM change is requested on your account.

6.3 Blocking Spam and Unwanted Calls

Enable Call Shield in MyTelecom > Security to automatically filter known spam numbers. Report spam texts by forwarding them to 7726. Block individual numbers through your phone's built-in call blocking feature.

6.4 Data Privacy

NovaCell collects usage data to provide and improve services. You can view and manage your privacy settings in MyTelecom > Account > Privacy. You can opt out of marketing communications at any time. For full details, visit telecom.example.com/privacy.
"""


def generate_pdf():
    """Generate a simple PDF from the guide text.

    Uses reportlab if available, otherwise falls back to fpdf2.
    """
    output_path = Path(__file__).parent / "data" / "telecom_guide.pdf"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from fpdf import FPDF

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Helvetica", size=10)

        # Replace unicode chars unsupported by core fonts
        clean_text = GUIDE_TEXT.strip().replace("\u2014", "-").replace("\u2013", "-").replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')

        for line in clean_text.split("\n"):
            if line.startswith("Chapter") or line.startswith("NovaCell Telecom"):
                pdf.set_font("Helvetica", "B", 14)
                pdf.multi_cell(w=190, h=10, text=line.strip())
                pdf.set_font("Helvetica", size=10)
            elif line.startswith("---") or line.startswith("==="):
                continue
            elif line.strip() == "":
                pdf.ln(3)
            else:
                pdf.multi_cell(w=190, h=5, text=line.strip())

        pdf.output(str(output_path))
        print(f"Generated PDF guide at {output_path}")

    except ImportError:
        # Fallback: write as plain text file with .pdf extension
        # (PyPDF can still read text from it for chunking purposes)
        output_path.write_text(GUIDE_TEXT.strip(), encoding="utf-8")
        print(f"fpdf2 not installed. Wrote plain-text guide to {output_path}")
        print("Install fpdf2 for proper PDF: pip install fpdf2")


if __name__ == "__main__":
    generate_pdf()
