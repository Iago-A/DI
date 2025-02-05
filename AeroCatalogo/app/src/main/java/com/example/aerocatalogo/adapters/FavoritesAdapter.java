package com.example.aerocatalogo.adapters;

import android.view.LayoutInflater;
import android.view.ViewGroup;

import androidx.annotation.NonNull;
import androidx.databinding.DataBindingUtil;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.aerocatalogo.R;
import com.example.aerocatalogo.databinding.ItemPlaneBinding;
import com.example.aerocatalogo.models.Plane;

import java.util.List;

public class FavoritesAdapter extends RecyclerView.Adapter<FavoritesAdapter.PlaneViewHolder> {
    private List<Plane> planes;
    private OnItemClickListener listener; // Cambiado a la interfaz propia

    public FavoritesAdapter(List<Plane> planes) {
        this.planes = planes;
    }

    public void updateFavorites(List<Plane> newFavorites) {
        this.planes.clear();
        this.planes.addAll(newFavorites);
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public FavoritesAdapter.PlaneViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        ItemPlaneBinding binding = DataBindingUtil.inflate(
                LayoutInflater.from(parent.getContext()),
                R.layout.item_plane,
                parent,
                false
        );
        return new PlaneViewHolder(binding);
    }

    @Override
    public void onBindViewHolder(@NonNull PlaneViewHolder holder, int position) { // Ahora usa el ViewHolder correcto
        Plane plane = planes.get(position);
        holder.bind(plane);
    }

    @Override
    public int getItemCount() {
        return planes != null ? planes.size() : 0;
    }

    public interface OnItemClickListener {
        void onItemClick(Plane plane);
    }

    class PlaneViewHolder extends RecyclerView.ViewHolder {
        private final ItemPlaneBinding binding;

        public PlaneViewHolder(@NonNull ItemPlaneBinding binding) {
            super(binding.getRoot());
            this.binding = binding;

            // Configurar el evento de clic
            binding.getRoot().setOnClickListener(v -> {
                Plane plane = binding.getPlane();
                if (plane != null && listener != null) {
                    listener.onItemClick(plane); // Llamamos al listener correctamente
                }
            });
        }

        public void bind(Plane plane) {
            binding.setPlane(plane);
            Glide.with(binding.getRoot().getContext())
                    .load(plane.getUrl())
                    .centerCrop()
                    .into(binding.planeImage);
            binding.executePendingBindings();
        }
    }
}
