package com.example.aerocatalogo.repositories;

import androidx.annotation.NonNull;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.example.aerocatalogo.models.Favorite;
import com.google.android.gms.tasks.Task;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class FavoritesRepository {
    private DatabaseReference userFavoritesRef;

    public FavoritesRepository(String userId) {
        userFavoritesRef = FirebaseDatabase.getInstance()
                .getReference("users/" + userId + "/favorites");
    }

    public Task<Boolean> toggleFavorite(String planeId) {
        return userFavoritesRef.child(planeId).get()
                .continueWithTask(task -> {
                    DataSnapshot snapshot = task.getResult();
                    boolean isFavorite = snapshot.exists();

                    return isFavorite
                            ? userFavoritesRef.child(planeId).removeValue()
                            .continueWith(removeTask -> false)
                            : userFavoritesRef.child(planeId).setValue(true)
                            .continueWith(addTask -> true);
                });
    }

    public LiveData<List<Favorite>> getFavorites() {
        MutableLiveData<List<Favorite>> favoritesLiveData = new MutableLiveData<>();

        userFavoritesRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                List<Favorite> favorites = new ArrayList<>();
                for (DataSnapshot child : snapshot.getChildren()) {
                    favorites.add(new Favorite(child.getKey(), true));
                }
                favoritesLiveData.setValue(favorites);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                favoritesLiveData.setValue(new ArrayList<>());
            }
        });

        return favoritesLiveData;
    }

    public LiveData<Boolean> isFavorite(String planeId) {
        MutableLiveData<Boolean> isFavoriteLiveData = new MutableLiveData<>();

        userFavoritesRef.child(planeId).addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                isFavoriteLiveData.setValue(snapshot.exists());
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                isFavoriteLiveData.setValue(false);
            }
        });

        return isFavoriteLiveData;
    }
}
