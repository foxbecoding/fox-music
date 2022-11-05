<template>
    <v-container class="px-4" fluid>
        <v-card color="rgb(12,12,12)">
            <v-card-title>
                Artists 
                <v-spacer></v-spacer>
            </v-card-title>
            <v-data-table
                style="background: rgb(12,12,12)"
                :headers="headers"
                :items="artists"
                :search="search"
            >
                <template v-slot:top>
                    <v-toolbar flat color="rgb(18,18,18)">
                        <v-btn @click="create" depressed color="primary">
                            Add New Artist
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
                <template v-slot:item.img_file_path="{ item }">
                    <v-avatar rounded="lg" size="40">
                        <v-img 
                            :src="`/assets/${item.img_file_path}`"
                            width="40"
                            contain
                        />
                    </v-avatar>
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
            <LibraryArtistsManageList
                @close="showDialog = false"
                @refreshData="refreshData"
                :showDialog="showDialog" 
                :artist="selectedArtist"
                :dialogType="dialogType"
                :dialogTitle="dialogTitle"
            />
        </v-card>
    </v-container>
</template>
<script lang="ts">
import Artist from '~/utils/types/Artists';
import Headers from '~/utils/types/Library/Headers';
import { defineComponent, ref, PropType} from '@nuxtjs/composition-api';

export default defineComponent({
    props: {
      artists: {
        type: Array as PropType<Artist[]>,
        required: true
      }
    },
	setup(props, context) {
        const search = ref<string>('');
        const dialogType = ref<string>('');
        const dialogTitle = ref<string>('');
        const showDialog = ref<boolean>(false);
        const selectedArtist = ref<Artist>({} as Artist);
        const headers = ref<Headers[]>([
            { text: 'Thumbnail', align: 'start', sortable: false, value: 'img_file_path'},
            { text: 'Name', value: 'name', align: '', sortable: true, },
            { text: 'Actions', value: 'actions', align: 'end', sortable: false },
        ]);

        //methods
        const create = (): void => {
            showDialog.value = true;
            dialogType.value = 'create';
            dialogTitle.value = 'Add new artist';
        };
        const update = (artist: Artist): void => {
            showDialog.value = true
            selectedArtist.value = artist;
            dialogType.value = 'update';
            dialogTitle.value = 'Update Artist';
        };
        const destroy = (artist: Artist): void => {
            showDialog.value = true;
            selectedArtist.value = artist;
            dialogType.value = 'delete';
            dialogTitle.value = 'Are you sure that you want to delete this artist?';
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
            selectedArtist,
            create,
            update, 
            destroy,
            refreshData 
        };
	},
})
</script>
