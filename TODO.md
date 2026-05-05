# Render Deployment TODO

## Completed
- [x] Commit changes (TODO.md)
- [x] Create .gitignore (ignores db.sqlite3, staticfiles, etc.)

## Next Steps
1. Run static collection: `python manage.py collectstatic --noinput`
2. Add .gitignore to git & commit: `git add .gitignore && git commit -m "Add .gitignore"`
3. Create GitHub repo (if none): Use GitHub website or gh CLI
4. Add remote & push: `git remote add origin https://github.com/USERNAME/jobseeker.git` (replace USERNAME), then `git push -u origin job`
5. On Render.com: New → Web Service → Connect GitHub repo → Python → Build: empty, Start: from Procfile → Add env vars (SECRET_KEY, etc.) → Create
6. Visit Render URL after deploy

Run next step?
