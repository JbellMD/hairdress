# Hairdresser Appointment System

A Django-based appointment scheduling system for hairdressers.

## Features

- Service management (haircuts, styling, coloring, etc.)
- Hairdresser profiles
- Appointment scheduling with time slot management
- Conflict prevention for overlapping appointments

## Setup

1. Clone the repository:
```bash
git clone https://github.com/JbellMD/hairdress.git
cd hairdress
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

For development, install additional dependencies:
```bash
pip install -r requirements-dev.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## Testing

Run tests with coverage:
```bash
./local_build.sh
```

## License

[MIT License](LICENSE)
