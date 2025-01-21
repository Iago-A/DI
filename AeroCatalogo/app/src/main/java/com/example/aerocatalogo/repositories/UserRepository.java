package com.example.aerocatalogo.repositories;

import com.example.aerocatalogo.models.User;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class UserRepository {
    // Necesitan de un constructor
    private final FirebaseAuth mAuth;
    private final DatabaseReference databaseRef;

    public UserRepository() {
        mAuth = FirebaseAuth.getInstance();
        databaseRef = FirebaseDatabase.getInstance().getReference("users");
    }

    public void registerUser(String fullName, String email, String phone, String address, String password, OnUserRegisteredListener listener) {
        // Crear usuario en Firebase Authentication
        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        FirebaseUser firebaseUser = mAuth.getCurrentUser();
                        if (firebaseUser != null) {
                            // Esperar a que la autenticación se complete

                            String uid = firebaseUser.getUid();
                            User newUser = new User(fullName, email, phone, address);

                            databaseRef.child(uid).setValue(newUser)
                                    .addOnSuccessListener(aVoid -> listener.onSuccess())
                                    .addOnFailureListener(listener::onFailure);
                        }
                    } else {
                        listener.onFailure(task.getException());
                    }
                });
    }

    public interface OnUserRegisteredListener {
        void onSuccess();
        void onFailure(Exception e);
    }
}
