.PHONY: setup build serve check clean migrate

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

