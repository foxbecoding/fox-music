<template>
    <v-dialog
        v-if="dialog"
        v-model="dialog"
        persistent
        max-width="320"
    >
        <v-card class="auth-card">
            <v-card-title>Update  Genre</v-card-title>
            <v-form
                class="mb-4 mx-4"
                ref="form"
                v-model="valid"
                lazy-validation
            >
                <v-text-field
                    v-model="name"
                    :rules="nameRules"
                    label="Genre name*"
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
import { $axios } from '~/utils/api';
import Cookies from 'universal-cookie';
import Genre from '~/utils/types/Genres';
import { RootState } from '@/store/index';
import { defineComponent, ref, watch, PropType, useStore} from '@nuxtjs/composition-api';

export default defineComponent({
    props: {
        genre: {
            type: Object as PropType<Genre>,
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
        const valid = ref<boolean>(true);
        const dialog = ref<boolean>(false);
        const name = ref<string>('');
        const nameRules = ref<any[]>([
            (v: any) => !! v || 'Genre name is required'
        ]);

        watch(props, () => {
            dialog.value = props.showDialog;
            name.value = props.dialogType == 'update' ? props.genre.name : ''
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
            if(!validate()){ return }
            interface PostData {
                name: string;
            }
            const postData: PostData = {
                name: name.value
            }

            try {
                const res = await $axios.$post(`${process.env.genresAPI}`, postData, {
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
                console.log(error) 
            }            
        };

        const update = async (csrftoken: string, auth_token: string): Promise<void> => {
            if(!validate()){ return }
            interface PostData {
                name: string;
            };
            const postData: PostData = {
                name: name.value
            };

            try {
                const res = await $axios.$put(`${process.env.genresAPI+props.genre.uniqid}/`, postData, {
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
                const res = await $axios.$delete(`${process.env.genresAPI+props.genre.uniqid}/`, {
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

        const close = (): void => {
            reset();
            context.emit('close', false);
        }; 

        const validate = () => {
            return form.value.validate();
        };

        const reset = (): void => {
            form.value.reset();
            form.value.resetValidation();
        };
        
		return {
            form,
            valid,
            dialog,
            name,
            nameRules,
            close,
            submit
		};
	},
})
</script>

