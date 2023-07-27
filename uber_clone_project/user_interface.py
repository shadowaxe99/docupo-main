import tkinter as tk
from tkinter import messagebox

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Über Clone")
        self.root.geometry("800x600")

        # Create frames for different sections of the UI
        self.registration_frame = tk.Frame(self.root)
        self.booking_frame = tk.Frame(self.root)
        self.payment_frame = tk.Frame(self.root)
        self.review_frame = tk.Frame(self.root)

        # Initialize UI elements
        self.init_registration_ui()
        self.init_booking_ui()
        self.init_payment_ui()
        self.init_review_ui()

    def init_registration_ui(self):
        # UI elements for user registration and authentication
        self.registration_frame.pack(fill="both", expand=True)
        self.username_entry = tk.Entry(self.registration_frame)
        self.password_entry = tk.Entry(self.registration_frame, show="*")
        self.login_button = tk.Button(self.registration_frame, text="Login", command=self.authenticateUser)
        self.signup_button = tk.Button(self.registration_frame, text="Sign Up", command=self.registerUser)

        # Layout
        self.username_entry.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.signup_button.pack()

    def init_booking_ui(self):
        # UI elements for ride booking
        self.booking_frame.pack(fill="both", expand=True)
        self.pickup_entry = tk.Entry(self.booking_frame)
        self.dropoff_entry = tk.Entry(self.booking_frame)
        self.book_button = tk.Button(self.booking_frame, text="Book Ride", command=self.bookRide)

        # Layout
        self.pickup_entry.pack()
        self.dropoff_entry.pack()
        self.book_button.pack()

    def init_payment_ui(self):
        # UI elements for payment integration
        self.payment_frame.pack(fill="both", expand=True)
        self.card_number_entry = tk.Entry(self.payment_frame)
        self.pay_button = tk.Button(self.payment_frame, text="Pay", command=self.processPayment)

        # Layout
        self.card_number_entry.pack()
        self.pay_button.pack()

    def init_review_ui(self):
        # UI elements for ratings and reviews
        self.review_frame.pack(fill="both", expand=True)
        self.review_text = tk.Text(self.review_frame)
        self.submit_button = tk.Button(self.review_frame, text="Submit Review", command=self.submitReview)

        # Layout
        self.review_text.pack()
        self.submit_button.pack()

    def registerUser(self):
        # Function for user registration
        from user import User
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.user = User(username, password)
        messagebox.showinfo("Success", "User registered successfully!")

    def authenticateUser(self):
        # Function for user authentication
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user.authenticate(username, password):
            messagebox.showinfo("Success", "User authenticated successfully!")
        else:
            messagebox.showerror("Error", "Authentication failed!")

    def bookRide(self):
        # Function for ride booking
        from ride import Ride
        pickup_location = self.pickup_entry.get()
        dropoff_location = self.dropoff_entry.get()
        self.ride = Ride(pickup_location, dropoff_location)
        self.ride.start_ride()
        messagebox.showinfo("Success", "Ride booked successfully!")

    def processPayment(self):
        # Function for payment processing
        from payment import Payment
        card_number = self.card_number_entry.get()
        self.payment = Payment(card_number)
        if self.payment.process_payment(100):
            self.ride.end_ride()
            messagebox.showinfo("Success", "Payment processed successfully!")
        else:
            messagebox.showerror("Error", "Payment failed!")

    def submitReview(self):
        # Function for submitting a review
        from review import Review
        review_text = self.review_text.get('1.0', 'end-1c')
        self.review = Review(self.user, review_text)
        if self.review.submit_review():
            messagebox.showinfo("Success", "Review submitted successfully!")
        else:
            messagebox.showerror("Error", "Review submission failed!")

if __name__ == "__main__":
    root = tk.Tk()
    ui = UserInterface(root)
    root.mainloop()
