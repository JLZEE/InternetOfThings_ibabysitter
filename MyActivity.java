package com.example.lenovo.myactivity;

import android.app.Activity;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ListView;

import java.util.ArrayList;


public class MyActivity extends Activity
{
    private ListView mList;
    private ArrayList<String> arrayList;
    private MyCustomAdapter mAdapter;
    private TCPClient mTcpClient;
    static boolean receive_from_server = false;
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        arrayList = new ArrayList<String>();

        //final EditText editText = (EditText) findViewById(R.id.editText);
        Button send = (Button)findViewById(R.id.send_button);
        Button disconnect = (Button)findViewById(R.id.disconnect_button);

        //relate the listView from java to the one created in xml
        mList = (ListView)findViewById(R.id.list);
        mAdapter = new MyCustomAdapter(this, arrayList);
        mList.setAdapter(mAdapter);

        // connect to the server
        new connectTask().execute("");
        if (mTcpClient != null) {
            String message = "Confirm1";
            //mAdapter.notifyDataSetChanged();
            mTcpClient.sendMessage(message);
            //receive_from_server=false;
        }

        disconnect.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                mTcpClient.stopClient();
            }
        });

        send.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //String message = editText.getText().toString();

                //add the text in the arrayList
                //arrayList.add("c: " + message);

                //sends the message to the server
                // && receive_from_server == true
                if (mTcpClient != null && receive_from_server == true) {
                    //mTcpClient.sendMessage(message);



                    String message = "OPEN FAN";
                    String shown = "Alert Confirmed and Fan Opened";
                    arrayList.add(shown);
                    mAdapter.notifyDataSetChanged();
                    mTcpClient.sendMessage(message);
                    receive_from_server = false;


                }

                //refresh the list

                //editText.setText("");
            }
        });

    }


    public class connectTask extends AsyncTask<String,String,TCPClient> {

        @Override
        protected TCPClient doInBackground(String... message) {

            //we create a TCPClient object and
            mTcpClient = new TCPClient(new TCPClient.OnMessageReceived() {
                @Override
                //here the messageReceived method is implemented
                public void messageReceived(String message) {
                    //this method calls the onProgressUpdate
                    publishProgress(message);
                }
            });
            mTcpClient.run();



            return null;
        }

        @Override
        protected void onProgressUpdate(String... values) {
            super.onProgressUpdate(values);

            //in the arrayList we add the messaged received from server
            arrayList.add(values[0]);
            receive_from_server = true;
            // notify the adapter that the data set has changed. This means that new message received
            // from server was added to the list
            mAdapter.notifyDataSetChanged();
        }
    }


}