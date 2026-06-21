"""Seed the tickets SQLite database with sample resolved support tickets."""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data" / "tickets.db"

TICKETS = [
    ("connectivity", "Customer reported complete loss of mobile signal indoors. Resolution: Advised customer to enable Wi-Fi calling via Settings > Phone > Wi-Fi Calling. Confirmed their plan supports Wi-Fi calling. Signal issue was due to building materials blocking cellular signal. Wi-Fi calling resolved the problem."),
    ("connectivity", "Customer complained about frequent disconnections from mobile data. Resolution: Ran a network diagnostic remotely. Found the customer was on a congested tower. Advised switching to 4G-only mode in Settings > Mobile Network > Preferred Network Type. Also toggled airplane mode to force reconnection to a less congested cell."),
    ("connectivity", "Customer said mobile data stopped working after traveling to a new city. Resolution: Checked account and found data roaming was disabled. Guided customer to Settings > Mobile Network > Data Roaming and toggled it on. Domestic roaming is included in all plans at no extra cost."),
    ("data", "Customer reported extremely slow data speeds of under 100 kbps. Resolution: Checked account and found the customer had exceeded their 20 GB high-speed data cap. Speed was throttled to 512 kbps per policy. Offered a 5 GB data top-up for $10 which restored full speed immediately."),
    ("data", "Customer could not connect to mobile data at all. Resolution: Verified APN settings were incorrect after a recent phone update. Guided customer to Settings > Mobile Network > Access Point Names and reset to default APN: internet.telecom.example.com. Data connection restored."),
    ("data", "Customer reported hotspot was not working for connected devices. Resolution: Confirmed the customer's plan included hotspot. The issue was the hotspot password contained special characters that the laptop couldn't handle. Changed the hotspot password to alphanumeric only and the connection worked."),
    ("roaming", "Customer was charged $450 for data usage while traveling in Canada. Resolution: Reviewed the account and found international roaming was active but no roaming bundle was purchased. Applied a courtesy credit of $200 and added the North America Roaming Bundle ($15/day) for the remainder of the trip."),
    ("roaming", "Customer could not make calls while traveling in Germany. Resolution: Checked account settings and found international roaming was not enabled. Enabled roaming remotely and activated the EU Roaming Bundle ($15/day). Advised the customer to restart their phone. Calls worked within 5 minutes."),
    ("roaming", "Customer asked about roaming charges before a trip to Japan. Resolution: Explained the Asia-Pacific Roaming Bundle at $20/day which includes 1 GB data, unlimited texts, and 60 minutes of calls. Without a bundle, data is $15/MB. Activated the bundle to start on the customer's departure date."),
    ("sim", "Customer's phone displayed 'SIM Not Detected' after dropping the phone. Resolution: Guided customer to power off, remove, and reinsert the SIM card. The SIM tray was slightly misaligned from the drop. Reseating fixed the issue. Advised getting a case to protect the SIM tray."),
    ("sim", "Customer wanted to switch from physical SIM to eSIM. Resolution: Verified the device supports eSIM (iPhone 14). Generated an eSIM QR code from the backend and emailed it to the customer. Guided them through Settings > Cellular > Add eSIM > Scan QR Code. Activation completed in 2 minutes."),
    ("sim", "Customer's number porting from another carrier was stuck for 3 days. Resolution: Found the port request was rejected because the account number provided was incorrect. Corrected the account number with the losing carrier and resubmitted. Port completed in 45 minutes."),
    ("billing", "Customer was double-billed for their monthly plan. Resolution: Confirmed two identical charges on the account due to a payment processing glitch. Issued an immediate refund for the duplicate charge. Refund appeared on the customer's card within 3-5 business days."),
    ("billing", "Customer disputed a $30 charge for premium SMS. Resolution: Found the customer had unknowingly subscribed to a horoscope service via SMS. Cancelled the subscription by texting STOP to the short code. Applied a one-time courtesy credit of $30. Enabled premium SMS blocking on the account."),
    ("billing", "Customer's plan auto-renewed at $85/month instead of the $65 promotional rate. Resolution: Verified the 12-month promotional period had ended. The plan reverted to the standard rate. Offered to re-apply a loyalty discount of $15/month for the next 6 months, bringing the price to $70/month."),
    ("billing", "Customer could not download their itemised bill from the app. Resolution: The issue was caused by a known bug in app version 4.2.1. Advised the customer to update to version 4.3.0 from the app store. After updating, the bill downloaded successfully as a PDF."),
    ("voice", "Customer reported echo during phone calls. Resolution: Echo is typically caused by a network delay or a faulty earpiece. Tested call quality by making a test call — echo was present. Advised the customer to disable VoLTE temporarily via Settings > Mobile Network > VoLTE. Echo stopped. Escalated a VoLTE compatibility ticket for their device model."),
    ("voice", "Customer could not receive incoming calls but could make outgoing calls. Resolution: Checked call forwarding settings and found all calls were being forwarded to voicemail. Disabled unconditional call forwarding by dialing ##21# from the customer's phone. Incoming calls resumed immediately."),
    ("voice", "Customer reported poor call quality and choppy audio. Resolution: The customer was in a low-signal area (1 bar). Advised enabling Wi-Fi calling for indoor use. Also ran a remote diagnostic that showed packet loss on the nearest tower. Filed a network quality report for the tower. Temporary fix via Wi-Fi calling worked well."),
    ("device", "Customer's phone was locked to our network and they wanted to switch carriers. Resolution: Verified the device was purchased 8 months ago and fully paid off. Submitted an unlock request. The device was unlocked remotely within 2 hours. Customer confirmed they could use another carrier's SIM."),
    ("device", "Customer reported their phone overheating when using mobile data. Resolution: Checked for known issues with the device model (Samsung Galaxy S23). Advised the customer to close background apps, disable unused features like Bluetooth and NFC, and ensure the phone's software was up to date. Overheating reduced after closing 12 background apps."),
    ("account", "Customer could not log in to the MyTelecom app. Resolution: The customer had changed their phone number recently and the app login was still tied to the old number. Updated the account's primary contact number in the system. Customer was able to log in with the new number and reset their password."),
    ("account", "Customer reported an unauthorised plan change on their account. Resolution: Investigated and found the plan was changed via the app by someone who had access to the customer's login. Reset the account password, enabled two-factor authentication, and reverted the plan to the original. No charges were applied for the unauthorised change."),
    ("account", "Customer wanted to transfer account ownership to a family member. Resolution: Explained the transfer process: both parties must visit a store with valid photo ID. There is no transfer fee. The new owner assumes all remaining device payments if any. Scheduled an appointment at the nearest store."),
]


def seed_database():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            resolution TEXT NOT NULL
        )
        """
    )

    cur.execute("SELECT COUNT(*) FROM tickets")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO tickets (category, resolution) VALUES (?, ?)", TICKETS
        )
        print(f"Inserted {len(TICKETS)} tickets into {DB_PATH}")
    else:
        print(f"Tickets table already populated ({DB_PATH})")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    seed_database()
