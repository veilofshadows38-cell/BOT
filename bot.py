import os
import time
import datetime
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "8573280925:AAHlT2QIZTvFbFyV4YgGR56cuz_-4ld-Yy4"
CHAT_ID = -1002659872445


BASE_PATH = "images"

# ==============================
#   EXACT MESSAGES (NO CHANGES!)
# ==============================
MESSAGES = [
    (
        """👍👍👍👍👍👍👍👍👍

👉 Win Up To ₹9999 Daily on WR777! 🎉

🌟 Spin the lucky wheel every day and win exciting cash rewards — up to ₹9999 in a single spin! 🌟

✅ Daily chances 🎯
✅ Multiple prize levels 🎁
✅ Big rewards, instant wins 🪙

💎 Why everyone loves WR777:
✅ 100% Safe 🔓 
✅ Fast Deposit/Withdrawal ⚡️
✅ 24/7 Online Support ⏰

🚩 Start spinning for BIG rewards! 💌

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo1.jpg"
    ),

    (
        """🎉GET ₹500 FREE on 🚩🚩🚩‼️

Spin the Lucky Wheel and win exciting cash rewards instantly!

🎰 Feeling Lucky?
Join WR777 today and enjoy 1️⃣ Free Spin — win up to ₹500 on the spot!
Every spin gives you a chance to grab cash, coins, or bonus rewards!

🔥 How to Get Your Free ₹500:
1️⃣ Register on WR777
2️⃣ Use your FREE SPIN
3️⃣ Win cash instantly
4️⃣ Invite friends to earn more!

✅ Free Spin Rewards
✅ Up to ₹500 Free
✅ 100% Safe & Trusted
✅ Fast Deposit/Withdrawal
✅ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo2.jpg"
    ),

    (
        """🏦 Bank Delay? Don’t Worry — WR777 Pays You! 💰

WR777 offers up to ₹399 compensation whenever your bank withdrawal is delayed.

💰 Compensation Chart (Based on delay & withdrawal amount):
🛡 ₹100–₹999 → ₹9 / ₹19 / ₹39
🛡 ₹1000–₹4999 → ₹19 / ₹39 / ₹99
🛡 ₹5000–₹50000 → ₹99 / ₹199 / ₹399

☄️ Fast Deposit & Withdrawal
🔒 100% Safe
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo3.jpg"
    ),

    (
        """💰 Get High Bonuses on Your First Deposit! 💰

Make your first deposit on WR777 and receive instant rewards up to ₹5777! 🎁

💰 Bonus Examples:
💱 Deposit ₹100 → Get ₹37
💱 Deposit ₹1000 → Get ₹177
💱 Deposit ₹5000 → Get ₹777
💱 Deposit ₹50000 → Get ₹5777 

✔️ Fast Deposit & Withdrawal 💥
✔️ 100% Safe & Trusted 🆒
✔️ 24/7 Online Support ⏰

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo4.jpg"
    ),

    (
        """🔔 Free Bonus ₹188 — Just Share on Social Media! 🔔

📲 Share WR777 and get a free ₹188 bonus! ✅

⏰ How to Claim:
➡️ Share → Wait 2 hours → Contact Customer Service
➡️ You can claim once every day
➡️ Activity Time: 08:00 - 22:00

💎 100% Safe
🌟 Fast Deposit/Withdrawal
🕒 24/7 Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo5.jpg"
    ),

    (
        """🔔 Enjoy Bonus on Every Deposit! 💱

Deposit anytime on WR777 and get an instant extra bonus added to your balance — unlimited times!

💰 More deposits = more bonus
⚡️ Fast Deposit & Withdrawal
🔓 100% Safe & Trusted
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo6.jpg"
    ),

    (
        """⭐⭐ Easy UPI Deposit Guide (WR777)

Follow these 4 simple steps to deposit quickly:
1️⃣ Screenshot the QR
2️⃣ Open PhonePe → Tap Scan
3️⃣ Select Upload QR → Choose your screenshot
4️⃣ Complete payment → Copy the UPI Ref No and submit

💯 100% Safe
💎 Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo7.jpg"
    ),

    (
        """👑 Unlock Elite VIP Rewards at WR777! 👑

🎆 Level up your tier and enjoy weekly bonuses, upgrade rewards, and free daily withdrawals — up to ₹59,999 when you reach VIP!

✅ VIP Benefits Include:
➡️ Weekly Bonus up to ₹1,777
➡️ Level Upgrade Bonus up to ₹59,999
➡️ Free Withdrawals: 2–10 times daily
➡️ Exclusive Monday VIP Rewards

🔒 100% Safe
☄️ Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo8.jpg"
    ),

    (
        """🔗 Invite Friends & Earn Up to ₹15,000/Month! ✨

Earn money daily just by sharing your WR777 invite link! 🎁

💸 Rewards:
🟠 You get ₹50 per invite
🟠 Your friend gets ₹20
🟠 Up to 10 invites/day = ₹500 daily

📌 How to Join:
1️⃣ Register on WR777 📲
2️⃣ Share your invite link 😀
3️⃣ Friend registers + deposits ₹100 🎉

Rewards credited instantly

🔒 💯 Safe | ⚡ Fast Withdrawal | ⏰ 24/7 Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo9.jpg"
    ),

    (
        """🔗 Become an Agent & Start Earning with WR777! 💎

🔔 Build your own team and earn commissions from 3 levels of sub-agents — bigger network = bigger income!

💼 Commission Rates:
✅ LV1 Subordinates: 0.30% – 0.70%
✅ LV2 Subordinates: 0.15% – 0.25%
✅ LV3 Subordinates: 0.07% – 0.15%

➡️ Earn daily, weekly, monthly passive income with zero investment!

🔓 100% Safe
⚡️ Fast Deposit/Withdrawal
⏰ 24/7 Online Support

☁️ Online Customer Service (https://wr777cs.com/)
👍 Telegram Customer Service (https://t.me/WR777CUSTOMERSERVICE)

📱 Download link - https://invite.wr777.club/?code=3UIHYPS
""",
        "photo10.jpg"
    ),
]

# ==============================
#   AUTO SEND — 8 AM + 30 MIN
# ==============================
def auto_scheduler(bot):
    msg_index = 0
    started_today = False

    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time == "08:00":
            started_today = True
            msg_index = 0
            print("Starting scheduled messages for today!")

        if started_today:
            message, photo_name = MESSAGES[msg_index]
            photo_path = os.path.join(BASE_PATH, photo_name)

            try:
                if os.path.exists(photo_path):
                    with open(photo_path, "rb") as f:
                        bot.send_photo(chat_id=CHAT_ID, photo=f, caption=message)
                else:
                    bot.send_message(chat_id=CHAT_ID, text=message)

                print(f"Sent message #{msg_index + 1}")

            except Exception as e:
                print("SEND ERROR:", e)

            msg_index += 1

            if msg_index >= len(MESSAGES):
                print("All 10 messages sent. Waiting for next day.")
                started_today = False
            else:
                time.sleep(60 * 30)

        else:
            time.sleep(20)


def start(update, context):
    update.message.reply_text("Bot is running 24/7 with scheduled messages!")


def start_bot():
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))

    import threading
    threading.Thread(target=auto_scheduler, args=(updater.bot,), daemon=True).start()

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    start_bot()
