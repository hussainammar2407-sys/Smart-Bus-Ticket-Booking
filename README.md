# Smart Bus Ticket Booking & Reservation System

## Project description

A beginner-friendly Python console application for viewing bus routes, finding
routes, booking seats, cancelling bookings, and checking a booking report.
Route and booking information is kept in memory while the application is
running.

## Features

- Lists five bus routes with departure times, fares, seat availability, and
  availability status.
- Searches routes by route ID, departure city, or destination city.
- Validates passenger name, age, seat count, route ID, and menu choices.
- Creates unique booking IDs and calculates the total fare.
- Prevents bookings for more seats than are available.
- Cancels a confirmed booking once and restores its seats.
- Shows confirmed and cancelled bookings in booking history.
- Reports total, confirmed, and cancelled bookings, reserved seats, and
  confirmed revenue.
- Displays the route schedule grouped by departure city.

## How to run

1. Open this project folder in VS Code.
2. Open the integrated terminal in the project folder.
3. Run `python main.py` (on some Windows installations, use `py main.py`).
4. Enter a menu number and follow the prompts.

The application uses only built-in Python features; no packages need to be
installed. Data is reset when the program exits.

## Python concepts used

- Lists and dictionaries for routes and booking records.
- A tuple for the supported city names and a set for used booking IDs.
- Functions, loops, conditionals, and formatted output.
- `enumerate()` for iterating over displayed routes.
- `break` to exit, `continue` to skip other departure cities, and `for-else`
  for route lookup.
- String methods such as `strip()`, `upper()`, and `casefold()`.
- `try`/`except` to handle invalid numeric input without crashing.

## Limitations

- Routes and bookings are stored in memory and disappear when the program
  closes.
- This is a single-user console demonstration; it has no database, GUI, login,
  online payment, or multi-user reservation locking.
- A booking stores one passenger name and age for the requested seat count.

## 3–5 minute demo guide

1. Choose **1** to show all five routes, fares, times, and seat statuses.
2. Choose **2**, then search for `Karachi` to show matching departures.
3. Choose **3**, enter `R101`, a passenger name, age `20`, and `2` seats.
   Explain the generated booking ID, fare calculation, and reduced availability.
4. Choose **5** to show the confirmed booking, then **6** to show the report.
5. Choose **4** and cancel using the booking ID from step 3. Try cancelling it
   again to demonstrate duplicate-cancellation protection.
6. Choose **7** for the grouped schedule, then **8** to exit.
