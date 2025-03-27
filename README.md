## 🧠 **Projekti nimi:**  
**Mentor** – Interaktiivne Õppimise ja Küsitluse Platvorm

---

## 🎯 **Projekti eesmärk:**

Luua veebipõhine süsteem, kus:
- **Õpilane saab esitada küsimusi** õpitud materjali kohta
- Vastab **ChatGPT (AI)** ja õpetaja saab lisada **isikliku kommentaari**
- Õpetaja näeb kõiki õpilaste küsimusi ja haldab kommentaare
- Õpilasi saab lisada, kinnitada ja neile saata parool e-kirjaga
- Django adminpaneel on **visuaalselt isikupärastatud ja tumerežiimiga**
- Kasutajal on **3-režiimiline teemalüliti**: hele, tume, süsteemne

---

## ⚙️ **Tehnoloogia ja tööriistad:**

- **Python 3.10**  
- **Django 5.1.7**  
- **SQLite** (või laiendatav PostgreSQL-ile)  
- **Bootstrap 4** (kujundus)  
- **ChatGPT API** (küsimustele vastamiseks)  
- **Custom Django Admin** (tumerežiim, logo, kujundus)

---

## 👥 **Kasutajate rollid:**

| Roll       | Õigused ja vaated                               |
|------------|--------------------------------------------------|
| **Õpilane** | Saab esitada küsimusi ja näha vastuseid/kommentaare |
| **Õpetaja** | Näeb kõiki küsimusi, lisab kommentaare, lisab/kinnitab õpilasi |
| **Admin**   | Täielik ligipääs Django adminpaneelile ja andmetele |

---

## ✍️ **Funktsioonid kokkuvõtlikult:**

### 🔹 Õpilase vaates:
- Küsimuse esitamine
- ChatGPT vastus
- Õpetaja kommentaar nähtav
- “Minu küsimused” logi
- Teemalüliti (☀️/🌙/🖥)

### 🔹 Õpetaja vaates:
- **Õpilaste lisamine** eraldi vormiga (adminita)
- E-posti teel **ajutise parooli saatmine**
- **Juhtpaneel**: nimekiri, küsimuste arv, kinnitamata kasutajad
- **Küsimuste logi** collapse/expand vaates
- **Kommentaaride lisamine** otse küsimustele

### 🔹 Django Admin:
- Täielik **tume kujundus vaikimisi**
- **Isikupärane logo ja jalus**
- **3-režiimiline lüliti** (cookie põhine)
- **Õpilase profiilil** näha kõik tema küsimused
- **QuestionLog** haldus + otsing + filtreerimine

---

## 🧩 **Struktuur (failid ja mallid):**

| Fail / Kaust             | Kirjeldus                           |
|--------------------------|-------------------------------------|
| `base.html`              | Ühine baas Bootstrap + nav           |
| `home.html`              | Õpilase küsimuste esitamise leht    |
| `teacher_dashboard.html` | Õpetaja juhtpaneel + statistika     |
| `add_student.html`       | Õpilase lisamise vorm õpetajale     |
| `my_questions.html`      | Õpilase isiklik küsimuste logi      |
| `teacher_question_log.html` | Küsimuste logi + kommentaaride vorm  |
| `admin_dark.css` / `admin_light.css` | Teemade stiilifailid          |
| `theme_toggle.js`        | Teemalüliti JS                      |

---

## 🧠 **Lisavõimalused edasi arendamiseks:**

- 📊 **Statistika vaade** (aktiivsus, küsimuste arv, kommenteerimisprotsent)
- 📎 PDF/CSV eksport õpilase või klassi kohta
- 💬 Õpilase ja õpetaja **vestluslogi ajajoonena**
- 🔐 2FA autentimine õpetajatele
- 🔄 AI vastuste järelhindamine / märgistamine “õige/vajab parandust”
- 🌍 Mitmekeelsus (nt eesti/inglise)

---

Kui soovid, võin sellest resümeest teha ka PDF-faili või panna selle `about.html` või `admin_dashboard.html` alla nähtavaks.

Kas soovid? 😊
