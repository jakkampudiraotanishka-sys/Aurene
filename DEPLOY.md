# Put Aurene online (free, ~15 minutes)

You'll end up with a link like **https://aurene.streamlit.app** that anyone can open
on phone or laptop — and the camera works because it's HTTPS.

---

## Step 1 — Get a Gemini API key (free)
1. Go to **https://aistudio.google.com/apikey** and sign in with Google.
2. Click **Create API key** and copy it. Keep it private.

## Step 2 — Put the code on GitHub
1. Create a free account at **https://github.com** (skip if you have one).
2. Click **+ → New repository**. Name it `aurene`, set it to **Public**, click **Create repository**.
3. On the new repo page click **uploading an existing file**.
4. Unzip `aurene.zip` on your computer, open the `aurene` folder, select **everything inside it**
   (including the `pages` and `.streamlit` folders) and drag it into the browser.
   - On Mac, press `Cmd + Shift + .` in Finder to see the hidden `.streamlit` folder.
   - On Windows, turn on View → Show → Hidden items.
5. Click **Commit changes**.

Your repo should look like:
```
app.py
home.py
navigation.py
stylist_ai.py
catalog.py
requirements.txt
pages/      (shop.py, restyle.py, community.py, donate.py, credits.py, impact.py)
.streamlit/ (config.toml, secrets.toml.example)
```

## Step 3 — Deploy on Streamlit Community Cloud
1. Go to **https://share.streamlit.io** and sign in **with GitHub**.
2. Click **Create app → Deploy a public app from GitHub**.
3. Repository: `your-username/aurene` · Branch: `main` · Main file path: **`app.py`**
4. **App URL:** type the name you want, e.g. `aurene` → `https://aurene.streamlit.app`
   (if taken, try `aurene-style`, `aurene-fashion`, etc.)
5. Open **Advanced settings → Secrets** and paste:
   ```
   GEMINI_API_KEY = "paste-your-key-here"
   ```
6. Click **Deploy**. The first build takes 2–5 minutes.

Done — share the link! 🎉

---

## Updating the site later
Edit a file on GitHub (or upload a new version) → the app redeploys automatically in about a minute.

## Good to know
- **Sleeping:** free apps go to sleep after a few days without visitors. The first visitor
  sees a "wake up" button; it takes ~30 seconds.
- **Phone camera:** the "Take a photo" tab uses the browser camera (often the front one on phones).
  The "Upload photos" tab on a phone offers "Take Photo", which uses the back camera — better for clothes.
- **Privacy:** photos are only kept in the visitor's browser session and sent to Google Gemini to
  generate styling. They're not saved anywhere by the app.
- **Gemini limits:** the free tier has a daily request limit. If lots of people use it, you may need to
  enable billing in Google AI Studio.

## Want your own .com domain?
Streamlit Community Cloud only gives `yourname.streamlit.app` addresses — it can't connect a domain
you've bought. Options if you want `aurene.com` / `aurene.in`:
1. **Easiest:** keep the free Streamlit app and set your domain to *forward/redirect* to it
   (most domain sellers like GoDaddy, Namecheap, Hostinger have a "Domain forwarding" setting).
2. **Proper custom domain:** host on **Render** or **Railway** (paid, a few dollars a month),
   which let you attach your domain directly. Start command:
   `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
   and add `GEMINI_API_KEY` as an environment variable / secret there.

## Run it on your own computer (optional)
```
pip install -r requirements.txt
copy .streamlit/secrets.toml.example to .streamlit/secrets.toml and add your key
streamlit run app.py
```
