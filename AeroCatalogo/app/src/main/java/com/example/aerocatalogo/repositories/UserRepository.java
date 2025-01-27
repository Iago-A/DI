package com.example.aerocatalogo.repositories;

import android.util.Log;

import androidx.annotation.NonNull;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.example.aerocatalogo.models.User;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

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
                        FirebaseUser firebaseUser = mAuth.getCurrentUser(); /////////////////////////
                        if (firebaseUser != null) {
                            // Esperar a que la autenticación se complete

                            String uid = firebaseUser.getUid(); /////////////////////////
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


    public void loginUser(String email, String password, OnLoginListener listener) {
        mAuth.signInWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        listener.onSuccess();
                    } else {
                        listener.onFailure(task.getException());
                    }
                });
    }


    public interface OnLoginListener {
        void onSuccess();
        void onFailure(Exception e);
    }


    public void addFavorite(String planeId) {
        // Para obtener el uid
        FirebaseUser firebaseUser = mAuth.getCurrentUser();
        
        if (firebaseUser != null) {
            String uid = firebaseUser.getUid();

            DatabaseReference userFavoritesRef = FirebaseDatabase.getInstance()
                    .getReference("users/" + uid + "/favorites");

            // Añade el ID del avión a favoritos
            userFavoritesRef.child(planeId).setValue(true)
                    .addOnSuccessListener(aVoid -> Log.d("Firebase", "Favorite added successfully"))
                    .addOnFailureListener(e -> Log.e("Firebase", "Error adding favorite", e));
        }
        else {
            Log.w("Firebase", "User is not authenticated. Cannot add favorite.");
        }
    }


    public void removeFavorite(String planeId) {
        // Para obtener el uid
        FirebaseUser firebaseUser = mAuth.getCurrentUser();

        if (firebaseUser != null) {
            String uid = firebaseUser.getUid();
            DatabaseReference userFavoritesRef = FirebaseDatabase.getInstance()
                    .getReference("users/" + uid + "/favorites");

            userFavoritesRef.child(planeId).removeValue()
                    .addOnSuccessListener(aVoid -> Log.d("Firebase", "Favorite removed successfully"))
                    .addOnFailureListener(e -> Log.e("Firebase", "Error removing favorite", e));
        } else {
            Log.w("Firebase", "User is not authenticated. Cannot remove favorite.");
        }
    }


    public LiveData<List<String>> getFavorites() {
        MutableLiveData<List<String>> favoritesLiveData = new MutableLiveData<>();
        FirebaseUser firebaseUser = mAuth.getCurrentUser();

        if (firebaseUser != null) {
            String uid = firebaseUser.getUid();
            DatabaseReference userFavoritesRef = FirebaseDatabase.getInstance()
                    .getReference("users/" + uid + "/favorites");

            userFavoritesRef.addValueEventListener(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot snapshot) {
                    List<String> favorites = new ArrayList<>();
                    for (DataSnapshot child : snapshot.getChildren()) {
                        favorites.add(child.getKey()); // Agrega el ID del favorito
                    }
                    favoritesLiveData.setValue(favorites); // Actualiza LiveData
                }

                @Override
                public void onCancelled(@NonNull DatabaseError error) {
                    Log.e("Firebase", "Error fetching favorites", error.toException());
                }
            });
        } else {
            Log.w("Firebase", "User is not authenticated. Cannot fetch favorites.");
        }

        return favoritesLiveData;
    }

}
