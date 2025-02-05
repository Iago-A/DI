package com.example.aerocatalogo.repositories;

import android.util.Log;

import androidx.annotation.NonNull;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.example.aerocatalogo.models.Plane;
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
    private DatabaseReference planesFavoritesRef;


    public FavoritesRepository(String userId) {
        userFavoritesRef = FirebaseDatabase.getInstance()
                .getReference("users/" + userId + "/favorites");
        planesFavoritesRef =FirebaseDatabase.getInstance().getReference("planes");
    }

    public Task<Boolean> toggleFavorite(Plane plane) {
        String planeId = plane.getId();

        return userFavoritesRef.child(planeId).get()
                .continueWithTask(task -> {
                    DataSnapshot snapshot = task.getResult();
                    boolean isFavorite = snapshot.exists();

                    return isFavorite
                            ? userFavoritesRef.child(planeId).removeValue()
                            .continueWith(removeTask -> false)
                            : userFavoritesRef.child(planeId).setValue(plane)
                            .continueWith(addTask -> true);
                });
    }

    public LiveData<List<Plane>> getFavorites() {
        MutableLiveData<List<Plane>> favoritesLiveData = new MutableLiveData<>();

        userFavoritesRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                List<String> favIds = new ArrayList<>();

                for (DataSnapshot child : snapshot.getChildren()) {
                    String planeId = child.getKey();
                    favIds.add(planeId);
                }

                    planesFavoritesRef.addValueEventListener(new ValueEventListener() {
                        final List<Plane> favorites = new ArrayList<>();
                        @Override
                        public void onDataChange(@NonNull DataSnapshot favSnapshot) {
                           for (String planeId : favIds) {
                               Plane plane = favSnapshot.child(planeId).getValue(Plane.class);
                               plane.setId(planeId);
                               favorites.add(plane);
                           }
                            favoritesLiveData.setValue(favorites);
                        }

                        @Override
                        public void onCancelled(@NonNull DatabaseError error) {

                        }
                    });
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
