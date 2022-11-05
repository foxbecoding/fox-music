<template>
    <v-dialog
        v-if="dialog"
        v-model="dialog"
        persistent
        max-width="320"
    >
        <v-card class="auth-card">
            <v-card-title>{{dialogTitle}}</v-card-title>
            <v-form
                v-if="dialogType == 'create' || dialogType == 'update'"
                class="mb-4 mx-4"
                ref="form"
                v-model="valid"
                lazy-validation
            >
                <v-file-input
                    :multiple="false"
                    ref="file-upload"
                    label="Upload artist image*"
                    accept="image/jpeg"
                    :error-messages="imageFileErrorMessage"
                    @change="setFile"
                    
                >
                    <template v-slot:selection="{ text }">
                        <v-chip
                            label
                            outlined
                            pill
                            color="primary"
                        >
                            {{ text }}
                        </v-chip>
                    </template>
                </v-file-input>
                <v-text-field
                    v-model="name"
                    :rules="nameRules"
                    label="Artist name*"
                    type="text"
                    required
                ></v-text-field>  
            </v-form>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="close" text color="blue">Close</v-btn>
                <v-btn @click="submit" text color="blue">Submit</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>
<script lang="ts">
import Cookies from 'universal-cookie';
import Artist from '~/utils/types/Artists';
import { $axios } from '~/utils/api';
import { RootState } from '@/store/index';
import { defineComponent, ref, watch, useStore, PropType} from '@nuxtjs/composition-api';

export default defineComponent({
    props: {
        artist: {
            type: Object as PropType<Artist>,
            required: true
        },
        showDialog: {
            type: Boolean,
            required: true
        },
        dialogType: {
            type: String,
            required: true
        },
        dialogTitle: {
            type: String,
            required: true
        },
    },
	setup(props, context) {
        const store = useStore<RootState>();
        const form = ref();
        const imageFile = ref<File>();
        const imageFileErrorMessage = ref('');
        const valid = ref<boolean>(true);
        const dialog = ref<boolean>(false);
        const name = ref<string>('');
        const nameRules = ref<any[]>([
            (v: any) => !! v || 'Artist name is required'
        ]);

        watch(props, () => {
            dialog.value = props.showDialog
            name.value = props.dialogType == 'update' ? props.artist.name : ''
        });

        //methods
        const submit = async () =>{
            const cookies: Cookies = new Cookies();
            const csrftoken: string = cookies.get('csrftoken');  
            const auth_token: string = store.state.auth_token;
            if(props.dialogType == 'create'){
                create(csrftoken, auth_token)
            }else if(props.dialogType == 'update'){
                update(csrftoken, auth_token)
            }else{
                destroy(csrftoken, auth_token)
            }        
                       
        };

        const create = async (csrftoken: string, auth_token: string): Promise<void> => {
            if (!imageFile.value){
                imageFileErrorMessage.value = 'Add artist image';
                return 
            }; 
            if(!validate()){ return }; 
            var formData = new FormData();
            formData.append("img_file_path", imageFile.value as File);
            formData.append("name", name.value);
            try {
                const res = await $axios.$post(`${process.env.artistsAPI}`, formData, {
                    progress: true,
                    withCredentials: true,
                    headers: {
                        'accept': 'application/json',
                        'Content-Type': `application/json`,
                        "X-CSRFToken": csrftoken, 
                        "Authorization": "Token "+auth_token
                    }
                });
                context.emit('refreshData')
                store.commit('snackbar', {text: res.success_message, show: true})
            } catch (error) {
                console.log(error); 
            }       
        };

        const update = async (csrftoken: string, auth_token: string): Promise<void> => {
            if(!validate()){ return };          
            let putData: any;
            if(imageFile.value){
                putData = new FormData();
                putData.append("img_file_path", imageFile.value as File);
                putData.append("name", name.value);
            }else{
                putData = {name: name.value as string};
            } 
            try {
                const res = await $axios.$put(`${process.env.artistsAPI+props.artist.uniqid}/`, putData, {
                    progress: true,
                    withCredentials: true,
                    headers: {
                        'accept': 'application/json',
                        'Content-Type': `application/json`,
                        "X-CSRFToken": csrftoken, 
                        "Authorization": "Token "+auth_token
                    }
                });
                context.emit('refreshData');
                store.commit('snackbar', {text: res.success_message, show: true});
            } catch (error) {
                console.log(error); 
            }   
        };

        const destroy = async (csrftoken: string, auth_token: string): Promise<void> => {
            try {
                const res = await $axios.$delete(`${process.env.artistsAPI+props.artist.uniqid}/`, {
                    progress: true,
                    withCredentials: true,
                    headers: {
                        'accept': 'application/json',
                        'Content-Type': `application/json`,
                        "X-CSRFToken": csrftoken, 
                        "Authorization": "Token "+auth_token
                    }
                });
                context.emit('refreshData')
                store.commit('snackbar', {text: res.success_message, show: true})
            } catch (error) {
                console.log(error); 
            } 
        };

        const setFile = (e: File): void => {
            imageFile.value = e;
            imageFileErrorMessage.value = '';     
        };

        const close = (): void => {
            if(props.dialogType == 'create' 
            || props.dialogType == 'update'){ 
                reset(); 
            } 
            context.emit('close', false);
        }; 
   
        const validate = () => {
            return form.value.validate();
        };

        const reset = (): void => {
            form.value.reset();
            form.value.resetValidation();
            imageFileErrorMessage.value = '';
        };
        
		return {
            form,
            valid,
            dialog,
            name,
            nameRules,
            imageFileErrorMessage,
            close,
            submit,
            setFile,
		};
	},
})
</script>

