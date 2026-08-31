# 🎓 SUNJOB Math Major Skill v3.2

<!-- shields -->
<p align="center">
  <img src="https://img.shields.io/badge/Language-Farsi%20(Persian)-blue?style=flat-square" alt="Persian" />
  <img src="https://img.shields.io/badge/Compatible-Claude%20%7C%20ChatGPT-green?style=flat-square" alt="Claude & ChatGPT" />
  <img src="https://img.shields.io/badge/Version-3.2-orange?style=flat-square" alt="v3.2" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT" />
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square" alt="Production" />
</p>

<p align="center">
  <strong>اسکیل انتخاب رشته کنکور ریاضی با هوش مصنوعی</strong><br/>
  AI-powered structured guidance for <strong>انتخاب رشته</strong> (university major selection) in Iran's mathematics track (کنکور ریاضی)
</p>

<p align="center">
  <a href="https://sunjob.ir"><strong>🌐 SUNJOB Website</strong></a> ·
  <a href="https://t.me/Sunjob1"><strong>📱 Telegram</strong></a> ·
  <a href="https://sunjob.ir/test/holland"><strong>🧪 Holland Test</strong></a>
</p>

---

## 🇮🇷 فارسی — اسکیل تخصصی انتخاب رشته کنکور ریاضی

انتخاب رشته یکی از مهم‌ترین تصمیم‌های مسیر تحصیلی و شغلیه؛ اما خیلی وقت‌ها این تصمیم فقط بر اساس یک عدد گرفته می‌شه: **رتبه کنکور.**

در حالی که رتبه فقط یکی از داده‌های تصمیمه.

این Skill برای این ساخته شده که هوش مصنوعی در بررسی انتخاب رشته، تصویر کامل‌تری از فرد و گزینه‌های پیش‌رو داشته باشه؛ یعنی علاوه بر رتبه و امکان قبولی، موضوعاتی مثل **علاقه، توانایی، اهداف شغلی، شرایط فردی، ویژگی‌های رشته‌ها و مسیر شغلی آینده** هم وارد تحلیل بشن.

هدف اینه که هوش مصنوعی فقط جواب نده:

> «با این رتبه چی میارم؟»

بلکه بتونه کمک کنه به سؤال مهم‌تری برسیم:

> «با توجه به شرایط من، چه انتخاب‌هایی منطقی‌ترن و چرا؟»

---

### Skill دقیقاً چیه؟

به زبان ساده، Skill یک **دستورالعمل و چارچوب آماده برای هوش مصنوعی** (Claude, ChatGPT و سایر ابزارها) هست که بهش کمک می‌کنه کار انتخاب رشته رو منظم‌تر، عمیق‌تر و با روش مشخصی انجام بده.

SUNJOB Math Major Skill v3.2 همین ایده رو برای **انتخاب رشته گروه ریاضی** به کار می‌گیره.

---

### این Skill چه کمکی می‌کنه؟

| بُعد تحلیل | توضیح |
|---|---|
| 🧠 علایق و ویژگی‌های فردی | شخصیت، سبک کار، ترجیحات |
| 📚 توانایی‌ها و نقاط قوت | مهارت‌های تحلیلی، عملی، خلاقانه |
| 🎯 اهداف و علایق شغلی | محیط کار، سبک زندگی، درآمد |
| 🏙️ شهر و شرایط زندگی | مهاجرت، محدودیت‌های جغرافیایی |
| 🎓 ویژگی‌های رشته و مسیر تحصیل | محتوای دروس، تخصص، ارشد |
| 💼 مسیر شغلی و آینده کاری | بازار کار، کارآفرینی، ریسک |
| ⚖️ مزایا، معایب و ریسک‌ها | مقایسه واقع‌بینانه |
| 🧩 اطلاعاتی که کم داریم | شناسایی نقاط کور |

---

### برای کیه؟

- 👨‍🎓 **داوطلبان کنکور ریاضی** — هر رتبه‌ای که دارن
- 📚 **دانش‌آموزان مردد** — بین چند رشته گیر کردن
- 🧠 **کسانی که فقط با رتبه تصمیم نمی‌گیرن** — می‌خوان عوامل بیشتری رو ببینن
- 🤖 **کاربران هوش مصنوعی** — Claude, ChatGPT, و سایر ابزارها

---

### چطور استفاده کنیم؟

1. فایل `SKILL.md` رو از این مخزن دریافت کن.
2. فایل رو در ابزار هوش مصنوعی‌ای که پشتیبانی می‌کنه قرار بده:
   - **Claude** → اضافه کردن به عنوان Claude Skill
   - **ChatGPT** → استفاده از `chatgpt/CHATGPT-MASTER-PROMPT.txt`
   - **سایر ابزارها** → System Instructions / Knowledge Files / Uploaded Files
3. اطلاعات خودت رو به هوش مصنوعی بده.
4. ازش بخواه با استفاده از این Skill شرایطت رو تحلیل کنه.
5. نمونه پرامپت‌ها رو ببین: [`examples/sample-prompts.md`](examples/sample-prompts.md)

---

### نمونه پرامپت سریع

```text
من داوطلب کنکور ریاضی هستم.

اول شرایط و ویژگی‌های من رو بررسی کن و اگر اطلاعات مهمی کم هست ازم سؤال بپرس.

بعد با استفاده از SUNJOB Math Major Skill v3.2،
رشته‌های مناسب‌تر برای من رو بررسی و مقایسه کن.

برای هر گزینه:
- دلیل پیشنهاد
- مزایا و معایب
- مسیر شغلی
- ریسک‌های احتمالی

اطلاعات من:
رتبه:
شهر مورد علاقه:
علایق:
توانایی‌ها:
هدف شغلی:
```

---

## 🇬🇧 English

### What Is This?

A **Claude Skill / ChatGPT Prompt** that turns any LLM into a structured, multi-dimensional **university major selection advisor** for Iranian mathematics-track students (کنکور ریاضی).

Instead of asking "what can I get with rank X?", this skill helps students explore:
- **Self-discovery**: interests, work style, values, personality
- **Career awareness**: real job paths, environments, growth potential
- **Decision framework**: structured comparison of 3–5 plausible directions
- **Bias detection**: prestige, family pressure, rank anxiety, social proof

### Repository Structure

| File / Directory | Description |
|---|---|
| `SKILL.md` | Core Skill definition — the main file you add to your AI tool |
| `manifest.json` | Skill metadata (name, version, language, entrypoint) |
| `chatgpt/` | ChatGPT-compatible master prompt and edition notes |
| `examples/` | 14 realistic test scenarios + ready-to-use sample prompts |
| `evaluations/` | Evaluation rubric and launch checklist |
| `references/` | Internal design docs (decision framework, research protocol, etc.) |

### What's New in v3.2

- **Opening discipline**: Guardrails to prevent the introduction from repeating in multi-turn conversations
- **Multi-turn continuity**: Natural conversation flow across turns without restarting
- **Recommendation confidence**: Explicit confidence calibration (strong / provisional / insufficient)
- **Psychometric interpretation**: Stricter discipline treating assessments as evidence, not verdicts
- **Minimum-variable protocol**: For rank questions, asks only variables that materially change the answer

### Installation

**Claude**: Upload the entire repository as a Claude Skill. Ensure `SKILL.md` is at the root.

**ChatGPT**: Copy the content of `chatgpt/CHATGPT-MASTER-PROMPT.txt` into a new chat.

**Other AI tools**: Load `SKILL.md` as System Instructions, Knowledge File, or equivalent.

### Links

- **SUNJOB Website**: [sunjob.ir](https://sunjob.ir)
- **Telegram**: [@Sunjob1](https://t.me/Sunjob1)
- **Holland Test**: [sunjob.ir/test/holland](https://sunjob.ir/test/holland)

---

## License

MIT — see [LICENSE](LICENSE).

---

<!--
  GitHub search indexing tags — انتخاب رشته کنکور ریاضی با هوش مصنوعی
  مشاوره انتخاب رشته | تحلیل رشته دانشگاهی | اسکیل کلود
  انتخاب رشته با هوش مصنوعی | konkur major selection AI
  دانشگاه صنعتی شریف | دانشگاه تهران | دانشگاه امیرکبیر
  مهندسی کامپیوتر | مهندسی برق | مهندسی مکانیک | ریاضی محض
  کارشناسی ارشد | دکتری | بازار کار | مسیر شغلی
  Holland test | MBTI | Big Five | test هالند
  سازمان سنجش | انتخاب رشته 1404 | کنکور 1404
  Claude skill Persian | ChatGPT prompt Persian
  AI education Iran | university admission Iran
  career counseling AI | major selection assistant
  prompt engineering Persian | فارسی
-->

<p align="center">
  <strong>SUNJOB Academy</strong> — کشف • تجربه • انتخاب<br/>
  <a href="https://sunjob.ir">sunjob.ir</a> · <a href="https://t.me/Sunjob1">Telegram</a>
</p>
