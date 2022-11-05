<template>
    <v-container class="px-4" fluid>
        <v-card color="rgb(12,12,12)">
            <v-card-title>
                Genres 
                <v-spacer></v-spacer>
            </v-card-title>
            <v-data-table
                style="background: rgb(12,12,12)"
                :headers="headers"
                :items="genres"
                :search="search"
            >
                <template v-slot:top>
                    <v-toolbar flat color="rgb(18,18,18)">
                        <v-btn @click="create" depressed color="primary">
                            Add New Genre
                        </v-btn>
                        <v-divider class="mx-4" inset vertical />
                        <v-spacer />
                        <v-text-field
                            v-model="search"
                            append-icon="mdi-magnify"
                            label="Search"
                            single-line
                            hide-details
                        /> 
                    </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                    <v-icon
                        small
                        class="mr-2"
                        color="warning"
                        @click="update(item)"
                    >
                        mdi-pencil
                    </v-icon>
                    <v-icon
                        small
                        color="red lighten-1"
                        @click="destroy(item)"
                    >
                        mdi-delete
                    </v-icon>
                </template>
            </v-data-table>
        </v-card>
        <LibraryGenresManageList 
            @close="showDialog = false"
            @refreshData="refreshData"
            :dialogTitle="dialogTitle"
            :dialogType="dialogType"
            :showDialog="showDialog" 
            :genre="selectedGenre"
        />
    </v-container>
</template>
<script lang="ts">
import Genre from '~/utils/types/Genres';
import Song from '~/utils/types/Songs';
import Headers from '~/utils/types/Library/Headers';
import { defineComponent, ref, PropType} from '@nuxtjs/composition-api';

export default defineComponent({
    props: {
      genres: {
        type: Array as PropType<Genre[]>,
        required: true
      }
    },
	setup(props, context) {
        const search = ref<string>('');
        const dialogType = ref<string>('');
        const dialogTitle = ref<string>('');
        const showDialog = ref<boolean>(false);
        const selectedGenre = ref<Genre>({
            name: '',
            uniqid: '',
            songs: [] as Song[]
        });
        const headers = ref<Headers[]>([
            { text: 'Name', value: 'name', align: 'start', sortable: false },
            { text: 'Actions', value: 'actions', align: 'end', sortable: false },
        ]);

        //methods
        const create = (): void => {
            showDialog.value = true;
            dialogType.value = 'create';
            dialogTitle.value = 'Add new artist';
        };
        const update = (genre: Genre): void => {
            showDialog.value = true
            selectedGenre.value = genre;
            dialogType.value = 'update';
            dialogTitle.value = 'Update Artist';
        };
        const destroy = (genre: Genre): void => {
            showDialog.value = true;
            selectedGenre.value = genre;
            dialogType.value = 'delete';
            dialogTitle.value = 'Are you sure that you want to delete this genre?';
        };
        const refreshData = (): void => {
            context.emit('refresh')
            showDialog.value = false
        };
		return {
            search, 
            headers, 
            showDialog,
            dialogType,
            dialogTitle,
            selectedGenre,
            create,
            update,
            destroy ,
            refreshData, 
        };
	},
})
</script>
