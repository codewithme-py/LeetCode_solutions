.PHONY: problem
problem:
	@if [ -z '$(filter-out problem,$(MAKECMDGOALS))' ]; then \
		echo 'Usage: make problem <problem_number>'; \
		exit 1; \
	fi
	@uv run scripts/create_problem.py $(filter-out problem,$(MAKECMDGOALS))

%:
	@:
