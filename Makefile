.PHONY: setup build serve check clean migrate install-hooks stats

setup:
	@bash scripts/bootstrap_mdbook.sh

build:
	@mdbook build

serve:
	@bash scripts/serve_local.sh

check:
	@bash scripts/ci_local.sh

clean:
	rm -rf book

migrate:
	@python3 scripts/migrate_to_mdbook.py

install-hooks:
	@mkdir -p .git/hooks
	@cp scripts/hooks/pre-commit .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@echo "Installed pre-commit hook: runs 'make check' before committing."

stats:
	@python3 scripts/book_stats.py
