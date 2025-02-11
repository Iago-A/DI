package com.example.aerocatalogo.repositories;

import androidx.annotation.NonNull;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.example.aerocatalogo.models.Plane;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;

public class DashboardRepository {
    private final FirebaseDatabase firebaseDatabase;
    private final MutableLiveData<List<Plane>> planesLiveData;
    private final MutableLiveData<String> errorLiveData;
    private ValueEventListener valueEventListener;

    public DashboardRepository() {
        firebaseDatabase = FirebaseDatabase.getInstance(); // Asegúrate de inicializar Firebase en tu app.
        planesLiveData = new MutableLiveData<>();
        errorLiveData = new MutableLiveData<>();
    }

    public LiveData<List<Plane>> getPlanesLiveData() {
        return planesLiveData;
    }

    public LiveData<String> getErrorLiveData() {
        return errorLiveData;
    }

    public void fetchPlanes() {
        // Para que después del logout el DashboardRepository no siga intentando escuchar cambios
        if (FirebaseAuth.getInstance().getCurrentUser() == null) {
            errorLiveData.setValue("Usuario no autenticado");
            return;
        }

        if (valueEventListener != null) {
            firebaseDatabase.getReference("planes").removeEventListener(valueEventListener);
        }


        valueEventListener = new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                List<Plane> planes = new ArrayList<>();
                for (DataSnapshot planeSnapshot : snapshot.getChildren()) {
                    // Obtener la clave que usaremos como id:
                    String planeId = planeSnapshot.getKey();

                    // Convierte el snapshot en un objeto Plane. Para qllo, la clase Plane debe tener un constructor vacío.
                    Plane plane = planeSnapshot.getValue(Plane.class);
                    if (plane != null) {
                        plane.setId(planeId);
                        planes.add(plane);
                    }
                }
                planesLiveData.setValue(planes);
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                errorLiveData.setValue("Error al obtener datos: " + error.getMessage());
            }
        };

        firebaseDatabase.getReference("planes").addValueEventListener(valueEventListener);
    }

    // Limpiar listener tras logout
    public void cleanup() {
        if (valueEventListener != null) {
            firebaseDatabase.getReference("planes").removeEventListener(valueEventListener);
            valueEventListener = null;
        }
        planesLiveData.setValue(null);
        errorLiveData.setValue(null);
    }
}
